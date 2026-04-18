function createSaleForm() {
    return {
        sku: '',
        description: '',
        discount: 0,
        submitSale: async function () {
            const response = await fetch('/sales/create', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    sku: parseInt(this.sku.trim()),
                    description: this.description,
                    discount: parseFloat(this.discount)
                })
            });
            if (response.ok) {
                alert('Sale created successfully!');
                window.location.href = '/sales';
            } else {
                const data = await response.json();
                alert(data.error);
            }
        }
    }
}