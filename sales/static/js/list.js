function listSales() {
    return {
        deleteSale(saleId) {
            if (confirm('Are you sure you want to delete this sale?')) {
                fetch(`/sales/delete/${saleId}`, {
                    method: 'DELETE'
                }).then(response => {
                    if (response.ok) {
                        location.reload();
                    }
                });
            }
        }
    }
}