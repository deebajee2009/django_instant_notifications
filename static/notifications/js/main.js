document.addEventListener('DOMContentLoaded', function () {
    const loginModalElement = document.getElementById('loginModal');
    const loginModal = new bootstrap.Modal(loginModalElement, {
        keyboard: false,
        backdrop: 'static'
    });

    const loginForm = document.getElementById('loginForm');
    const username = localStorage.getItem('username');

    if (username) {
        // If username exists, load the dashboard immediately
        loadDashboard(username);
    } else {
        // Otherwise, show the login modal
        loginModal.show();
    }

    // Handle login form submission
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const usernameInput = document.getElementById('usernameInput');
        const submittedUsername = usernameInput.value.trim();

        if (submittedUsername) {
            localStorage.setItem('username', submittedUsername);
            loginModal.hide();
            loadDashboard(submittedUsername);
        }
    });
});

/**
 * Triggers HTMX to fetch and load the dashboard content.
 * @param {string} username - The user's username.
 */
function loadDashboard(username) {
    const dashboardWrapper = document.getElementById('dashboard-wrapper');
    if (dashboardWrapper) {
        // Set HTMX attributes for the GET request
        dashboardWrapper.setAttribute('hx-get', `/dashboard/${username}/`);
        dashboardWrapper.setAttribute('hx-trigger', 'load'); // Trigger immediately
        dashboardWrapper.setAttribute('hx-swap', 'innerHTML');
        // Process the element to make HTMX aware of the new attributes
        htmx.process(dashboardWrapper);
    }
}

/**
 * Initializes components that exist only after the dashboard is loaded.
 * This function is called by the htmx:afterSwap event listener.
 * @param {string} username - The user's username.
 */
function initializeDashboardComponents(username) {
    console.log(`Initializing components for ${username}`);

    // Initialize Jalali date pickers on any input with data-jdp attribute
    jalaliDatepicker.startWatch();

    // Dynamically update HTMX attributes that depend on the username
    // Note: The websocket-handler is already processed by HTMX upon swap.
    const dateFilterForm = document.getElementById('date-filter-form');
    if (dateFilterForm) {
        dateFilterForm.setAttribute('hx-post', `/dashboard/${username}/`);
    }

    const backButton = document.querySelector(`[hx-get^="/dashboard/"]`);
    if(backButton) {
        backButton.setAttribute('hx-get', `/dashboard/${username}/`);
    }
}

// Listen for HTMX's afterSwap event. This is the correct way to initialize
// JS on content that has been loaded dynamically.
document.body.addEventListener('htmx:afterSwap', function(event) {
    const username = localStorage.getItem('username');
    if (username) {
        // The dashboard content has just been loaded into the DOM.
        // Now it's safe to initialize the components inside it.
        initializeDashboardComponents(username);
    }
});
