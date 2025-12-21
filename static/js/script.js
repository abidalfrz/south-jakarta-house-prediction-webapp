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
    
    alerts.forEach(function(alertElement) {
        setTimeout(function() {
            if (typeof bootstrap !== 'undefined') {
                const bsAlert = new bootstrap.Alert(alertElement);
                bsAlert.close();
            } else {
                alertElement.style.display = 'none';
            }
        }, 5000); 
    });

});