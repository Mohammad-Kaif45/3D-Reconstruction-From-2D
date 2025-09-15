/**
 * Efficient Theme Management System
 * Handles theme switching, persistence, and system preference detection
 */

class ThemeManager {
    constructor() {
        this.themeToggle = null;
        this.currentTheme = 'light';
        this.themes = ['light', 'dark'];
        this.storageKey = 'theme-preference';
        this.mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        
        this.init();
    }

    /**
     * Initialize the theme manager
     */
    init() {
        this.setupThemeToggle();
        this.loadTheme();
        this.setupMediaQueryListener();
        this.applyTheme();
    }

    /**
     * Setup theme toggle button
     */
    setupThemeToggle() {
        this.themeToggle = document.getElementById('theme-toggle');
        if (this.themeToggle) {
            this.themeToggle.addEventListener('click', () => this.toggleTheme());
            this.themeToggle.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    this.toggleTheme();
                }
            });
        }
    }

    /**
     * Load theme from storage or detect system preference
     */
    loadTheme() {
        // Try to load from localStorage first
        const storedTheme = localStorage.getItem(this.storageKey);
        
        if (storedTheme && this.themes.includes(storedTheme)) {
            this.currentTheme = storedTheme;
        } else {
            // Fall back to system preference
            this.currentTheme = this.mediaQuery.matches ? 'dark' : 'light';
        }
    }

    /**
     * Setup media query listener for system theme changes
     */
    setupMediaQueryListener() {
        this.mediaQuery.addEventListener('change', (e) => {
            // Only auto-switch if user hasn't manually set a preference
            if (!localStorage.getItem(this.storageKey)) {
                this.currentTheme = e.matches ? 'dark' : 'light';
                this.applyTheme();
            }
        });
    }

    /**
     * Toggle between light and dark themes
     */
    toggleTheme() {
        this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
        this.applyTheme();
        this.saveTheme();
        this.updateToggleButton();
        
        // Dispatch custom event for other components
        this.dispatchThemeChangeEvent();
    }

    /**
     * Apply the current theme to the document
     */
    applyTheme() {
        const root = document.documentElement;
        
        // Remove all theme classes first
        this.themes.forEach(theme => {
            root.classList.remove(`theme-${theme}`);
        });
        
        // Add current theme class
        root.classList.add(`theme-${this.currentTheme}`);
        
        // Set data attribute for CSS targeting
        root.setAttribute('data-theme', this.currentTheme);
        
        // Update meta theme-color for mobile browsers
        this.updateMetaThemeColor();
        
        // Update toggle button appearance
        this.updateToggleButton();
    }

    /**
     * Update the theme toggle button appearance
     */
    updateToggleButton() {
        if (!this.themeToggle) return;
        
        const icon = this.themeToggle.querySelector('i');
        if (icon) {
            if (this.currentTheme === 'dark') {
                icon.className = 'fas fa-sun';
                this.themeToggle.setAttribute('title', 'Switch to Light Mode');
            } else {
                icon.className = 'fas fa-moon';
                this.themeToggle.setAttribute('title', 'Switch to Dark Mode');
            }
        }
    }

    /**
     * Save theme preference to localStorage
     */
    saveTheme() {
        localStorage.setItem(this.storageKey, this.currentTheme);
    }

    /**
     * Update meta theme-color for mobile browsers
     */
    updateMetaThemeColor() {
        let metaThemeColor = document.querySelector('meta[name="theme-color"]');
        
        if (!metaThemeColor) {
            metaThemeColor = document.createElement('meta');
            metaThemeColor.name = 'theme-color';
            document.head.appendChild(metaThemeColor);
        }
        
        // Set appropriate color based on theme
        if (this.currentTheme === 'dark') {
            metaThemeColor.content = '#1a202c';
        } else {
            metaThemeColor.content = '#ffffff';
        }
    }

    /**
     * Dispatch custom event for theme changes
     */
    dispatchThemeChangeEvent() {
        const event = new CustomEvent('themechange', {
            detail: {
                theme: this.currentTheme,
                previousTheme: this.currentTheme === 'light' ? 'dark' : 'light'
            }
        });
        document.dispatchEvent(event);
    }

    /**
     * Get current theme
     */
    getCurrentTheme() {
        return this.currentTheme;
    }

    /**
     * Set theme programmatically
     */
    setTheme(theme) {
        if (this.themes.includes(theme)) {
            this.currentTheme = theme;
            this.applyTheme();
            this.saveTheme();
            this.dispatchThemeChangeEvent();
        }
    }

    /**
     * Check if current theme is dark
     */
    isDark() {
        return this.currentTheme === 'dark';
    }

    /**
     * Check if current theme is light
     */
    isLight() {
        return this.currentTheme === 'light';
    }

    /**
     * Reset to system preference
     */
    resetToSystem() {
        localStorage.removeItem(this.storageKey);
        this.currentTheme = this.mediaQuery.matches ? 'dark' : 'light';
        this.applyTheme();
        this.dispatchThemeChangeEvent();
    }
}

/**
 * Utility functions for theme-related operations
 */
const ThemeUtils = {
    /**
     * Add theme-aware class to element
     */
    addThemeClass: (element, lightClass, darkClass) => {
        if (!element) return;
        
        const themeManager = window.themeManager;
        if (themeManager.isDark()) {
            element.classList.add(darkClass);
            element.classList.remove(lightClass);
        } else {
            element.classList.add(lightClass);
            element.classList.remove(darkClass);
        }
    },

    /**
     * Toggle theme-aware class on element
     */
    toggleThemeClass: (element, lightClass, darkClass) => {
        if (!element) return;
        
        const themeManager = window.themeManager;
        if (themeManager.isDark()) {
            element.classList.toggle(darkClass);
        } else {
            element.classList.toggle(lightClass);
        }
    },

    /**
     * Get theme-aware color value
     */
    getThemeColor: (lightColor, darkColor) => {
        const themeManager = window.themeManager;
        return themeManager.isDark() ? darkColor : lightColor;
    }
};

/**
 * Initialize theme manager when DOM is ready
 */
document.addEventListener('DOMContentLoaded', () => {
    // Initialize theme manager
    window.themeManager = new ThemeManager();
    
    // Make theme utils available globally
    window.ThemeUtils = ThemeUtils;
    
    // Log theme initialization
    console.log('Theme Manager initialized with theme:', window.themeManager.getCurrentTheme());
});

/**
 * Handle theme changes for components that need to react
 */
document.addEventListener('themechange', (event) => {
    const { theme, previousTheme } = event.detail;
    console.log(`Theme changed from ${previousTheme} to ${theme}`);
    
    // You can add custom logic here for components that need to react to theme changes
    // For example, updating charts, maps, or other components that have their own theming
    
    // Example: Update any third-party components
    if (window.updateComponentThemes) {
        window.updateComponentThemes(theme);
    }
});

/**
 * Export for module systems (if needed)
 */
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { ThemeManager, ThemeUtils };
}
