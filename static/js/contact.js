// Hotel Nightingale — Contact Script
// Date validation for check-in / check-out fields

document.addEventListener('DOMContentLoaded', function () {
    const checkInInput = document.getElementById('id_check_in');
    const checkOutInput = document.getElementById('id_check_out');

    if (!checkInInput || !checkOutInput) {
        return;
    }

    const today = new Date().toISOString().split('T')[0];
    checkInInput.setAttribute('min', today);

    if (!checkOutInput.value) {
        checkOutInput.setAttribute('min', today);
    }

    checkInInput.addEventListener('change', function () {
        if (!checkInInput.value) {
            return;
        }

        const checkInDate = new Date(checkInInput.value);
        const nextDay = new Date(checkInDate);
        nextDay.setDate(nextDay.getDate() + 1);
        const minCheckOut = nextDay.toISOString().split('T')[0];

        checkOutInput.setAttribute('min', minCheckOut);

        if (checkOutInput.value && checkOutInput.value <= checkInInput.value) {
            checkOutInput.value = minCheckOut;
        }
    });
});
