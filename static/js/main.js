let webSocket = null;

document.addEventListener('DOMContentLoaded', function () {
    const loginModal = new bootstrap.Modal(document.getElementById('loginModal'), {
        keyboard: false,
        backdrop: 'static'
    });

    const loginForm = document.getElementById('loginForm');

    // Check if username exists in localStorage
    const username = localStorage.getItem('username');

    if (!username) {
        loginModal.show();
    } else {
        // If user is already "logged in", initialize the dashboard
        initializeDashboard(username);
    }

    // Handle login form submission
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const usernameInput = document.getElementById('usernameInput');
        const submittedUsername = usernameInput.value.trim();

        if (submittedUsername) {
            localStorage.setItem('username', submittedUsername);
            loginModal.hide();
            // Load dashboard content via HTMX after login
            htmx.ajax('GET', `/dashboard/${submittedUsername}/`, {target: 'body'});
            // We need to re-initialize after the content is loaded
            // Using a delay to ensure the DOM is updated. A better way would be using htmx events.
            setTimeout(() => initializeDashboard(submittedUsername), 500);
        }
    });
});

function initializeDashboard(username) {
    console.log(`Initializing dashboard for ${username}`);

    // Set username in navbar display
    const usernameDisplay = document.getElementById('username-display');
    if (usernameDisplay) {
        usernameDisplay.textContent = username;
    }

    // Dynamically set HTMX attributes that depend on the username
    updateHtmxAttributes(username);

    // Connect to WebSocket
    connectWebSocket(username);
}

function updateHtmxAttributes(username) {
    // Set post URL for date filter form
    const dateFilterForm = document.getElementById('date-filter-form');
    if (dateFilterForm) {
        dateFilterForm.setAttribute('hx-post', `/dashboard/${username}/`);
    }

    // Update back button on message detail page if it exists
    const backButton = document.querySelector(`[hx-get^="/dashboard/"]`);
    if(backButton) {
        backButton.setAttribute('hx-get', `/dashboard/${username}/`);
    }

    // Update WebSocket connection element
    const wsConnectElement = document.getElementById('websocket-handler');
    if(wsConnectElement) {
        wsConnectElement.setAttribute('ws-connect', `/ws/notifications/${username}/`);
        htmx.process(wsConnectElement); // Tell htmx to process the new attribute
    }
}

function connectWebSocket(username) {
    // This example uses htmx's built-in websocket extension,
    // which is simpler. Ensure your `<body>` or a persistent parent element
    // has `hx-ext="ws"` and `ws-connect="/ws/notifications/{username}/"`.
    // The `updateHtmxAttributes` function sets this dynamically.
    console.log("HTMX will handle the WebSocket connection.");
}


// Listen for htmx:afterSwap event to re-initialize after page navigation
document.body.addEventListener('htmx:afterSwap', function(event) {
    const username = localStorage.getItem('username');
    if (username) {
        initializeDashboard(username);
    }
});
