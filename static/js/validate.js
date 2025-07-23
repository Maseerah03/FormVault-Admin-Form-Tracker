document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('adminForm');

  form.addEventListener('submit', function (event) {
    const fullname = document.getElementById('fullname').value.trim();
    const department = document.getElementById('department').value;
    const requestType = document.getElementById('requestType').value;
    const reason = document.getElementById('reason').value.trim();
    const date = document.getElementById('date').value;

    // Check if all required fields are filled
    if (!fullname || !department || !requestType || !reason || !date) {
      alert('Please fill in all required fields.');
      event.preventDefault(); // Stop form from submitting
      return;
    }

    // Optional: check if reason is long enough
    if (reason.length < 10) {
      alert('Reason must be at least 10 characters long.');
      event.preventDefault();
      return;
    }
  });
});
