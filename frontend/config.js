// Frontend Configuration
// Update this file to change the backend API endpoint
const CONFIG = {
    API_BASE_URL: 'http://74.208.146.37:8080',
    // Alternative configurations:
    // API_BASE_URL: 'http://localhost:8080',           // For local development
    // API_BASE_URL: 'https://yourdomain.com/api',     // For production with SSL
};

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
