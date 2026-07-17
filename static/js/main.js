document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle');
    const wrapper = document.getElementById('wrapper');
    const sidebarLinks = document.querySelectorAll('#sidebar-wrapper .list-group-item');
    const contentSections = document.querySelectorAll('.content-section');
    const contentSectionCloses = document.querySelectorAll('.content-section-close');
    const greetingSection = document.getElementById('greeting-section');
    const emailIcon = document.getElementById('email-icon');
    const emailModal = new bootstrap.Modal(document.getElementById('emailModal'));
    const copyEmailBtn = document.getElementById('copyEmailBtn');

    // Sidebar toggle functionality
    if (menuToggle && wrapper) {
        menuToggle.addEventListener('click', function() {
            wrapper.classList.toggle('toggled');
        });
    }

    // Function to show a specific content section
    function showContentSection(sectionId) {
        // Hide all content sections first
        contentSections.forEach(section => {
            section.style.display = 'none';
            section.classList.remove('active');
        });
        // Hide greeting section
        if (greetingSection) {
            greetingSection.style.display = 'none';
        }

        // Show the selected section
        const targetSection = document.getElementById(sectionId);
        if (targetSection) {
            targetSection.style.display = 'block';
            // Trigger reflow to restart animation
            void targetSection.offsetWidth;
            targetSection.classList.add('active');
        }
    }

    // Handle sidebar link clicks
    sidebarLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1) + '-section';
            showContentSection(targetId);
        });
    });

    // Handle closing content sections
    contentSectionCloses.forEach(closeBtn => {
        closeBtn.addEventListener('click', function() {
            this.closest('.content-section').style.display = 'none';
            this.closest('.content-section').classList.remove('active');
            // Show greeting section again when all content sections are closed
            if (greetingSection) {
                greetingSection.style.display = 'flex';
            }
        });
    });

    // Handle clicks outside content sections to close them
    document.addEventListener('click', function(e) {
        contentSections.forEach(section => {
            if (section.classList.contains('active') && !section.contains(e.target) && !e.target.closest('#sidebar-wrapper')) {
                section.style.display = 'none';
                section.classList.remove('active');
                if (greetingSection) {
                    greetingSection.style.display = 'flex';
                }
            }
        });
    });

    // Email icon functionality
    if (emailIcon) {
        emailIcon.addEventListener('click', function(e) {
            e.preventDefault();
            emailModal.show();
        });
    }

    if (copyEmailBtn) {
        copyEmailBtn.addEventListener('click', function() {
            const emailAddress = document.querySelector('#emailModal h4').textContent;
            navigator.clipboard.writeText(emailAddress).then(() => {
                alert('Email address copied to clipboard!');
            }).catch(err => {
                console.error('Failed to copy email: ', err);
            });
        });
    }

    // Initial state: show greeting section
    if (greetingSection) {
        greetingSection.style.display = 'flex';
    }
});
