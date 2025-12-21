document.addEventListener("DOMContentLoaded", function() {

    const predictForm = document.getElementById('predictForm');
    if (predictForm) {
        predictForm.addEventListener('submit', function() {
            const btn = document.getElementById('btnSubmit');
            btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Analysing AI Model...';
            btn.disabled = true;
        });
    }

    const priceDisplay = document.getElementById('priceDisplay');
    if (priceDisplay) {
        const rawPrice = priceDisplay.dataset.price;
        if (rawPrice) {
            const formattedPrice = new Intl.NumberFormat('id-ID', {
                style: 'currency',
                currency: 'IDR',
                minimumFractionDigits: 0,
                maximumFractionDigits: 0
            }).format(rawPrice);
            priceDisplay.innerText = formattedPrice;
        }
    }
    
    setTimeout(function() {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            if (typeof bootstrap !== 'undefined') {
                let bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        });
    }, 5000);

});