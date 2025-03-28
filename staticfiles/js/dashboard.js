document.addEventListener("DOMContentLoaded", function () {
    console.log("Dashboard Loaded");

    // Smooth scrolling effect for nav links
    document.querySelectorAll('a.nav-link').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 50,
                    behavior: "smooth"
                });
            }
        });
    });

    // Hover effect on profile card for scaling
    let profileCard = document.querySelector('.card-body.text-center');
    if (profileCard) {
        profileCard.addEventListener('mouseover', function () {
            this.style.transform = 'scale(1.05)';
            this.style.transition = 'all 0.3s ease-in-out';
        });

        profileCard.addEventListener('mouseout', function () {
            this.style.transform = 'scale(1)';
        });
    }

    // Hover effect on profile image for scaling
    let profileImage = document.querySelector('.card-body.text-center img');
    if (profileImage) {
        profileImage.addEventListener('mouseover', function () {
            this.style.transform = 'scale(1.1)';
        });

        profileImage.addEventListener('mouseout', function () {
            this.style.transform = 'scale(1)';
        });
    }

    // Modal Animation (Add Course Modal)
    let addCourseModal = new bootstrap.Modal(document.getElementById('addCourseModal'));

    document.getElementById("addCourseModal").addEventListener("show.bs.modal", function () {
        console.log("Add Course Modal Opened");
    });
});

// dashboard.js
document.addEventListener('DOMContentLoaded', function() {
  // Add animation delay to course cards
  const courseCards = document.querySelectorAll('.col-md-6');
  courseCards.forEach((card, index) => {
    card.style.setProperty('--animation-order', index);
  });

  // Profile card animation
  const profileCard = document.querySelector('.col-md-3 .card');
  if (profileCard) {
    profileCard.style.setProperty('--animation-order', courseCards.length);
  }
});