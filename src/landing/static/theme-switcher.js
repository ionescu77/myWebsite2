/**
 * Theme Switcher - Minimal JavaScript for theme persistence
 * Supports light/dark themes and accent color switching
 */

(function() {
    'use strict';
    
    // Get saved preferences or use defaults
    var savedTheme = localStorage.getItem('theme') || 'dark';
    var savedAccent = localStorage.getItem('accent') || 'orange';
    
    // Apply theme immediately to prevent flash
    document.documentElement.setAttribute('data-theme', savedTheme);
    document.documentElement.setAttribute('data-accent', savedAccent);
    
    // Wait for DOM to be ready
    function ready(fn) {
        if (document.readyState !== 'loading') {
            fn();
        } else {
            document.addEventListener('DOMContentLoaded', fn);
        }
    }
    
    ready(function() {
        // Theme toggle buttons
        var themeBtns = document.querySelectorAll('.theme-btn');
        themeBtns.forEach(function(btn) {
            // Set active state
            if (btn.getAttribute('data-theme') === savedTheme) {
                btn.classList.add('active');
            }
            
            // Add click handler
            btn.addEventListener('click', function() {
                var theme = this.getAttribute('data-theme');
                document.documentElement.setAttribute('data-theme', theme);
                localStorage.setItem('theme', theme);
                
                // Update active state
                themeBtns.forEach(function(b) { b.classList.remove('active'); });
                this.classList.add('active');
            });
        });
        
        // Accent color buttons
        var accentBtns = document.querySelectorAll('.accent-color');
        accentBtns.forEach(function(btn) {
            // Set active state
            if (btn.getAttribute('data-color') === savedAccent) {
                btn.classList.add('active');
            }
            
            // Add click handler
            btn.addEventListener('click', function() {
                var accent = this.getAttribute('data-color');
                document.documentElement.setAttribute('data-accent', accent);
                localStorage.setItem('accent', accent);
                
                // Update active state
                accentBtns.forEach(function(b) { b.classList.remove('active'); });
                this.classList.add('active');
            });
        });
    });
})();
