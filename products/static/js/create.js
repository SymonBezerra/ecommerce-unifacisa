function createProductForm() {
    return {
        name: '',
        price: 0.0,
        type: '',
        description: '',
        expirationDate: '',
        submitProduct: async function () {
            const response = await fetch('/products/create', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: this.name,
                    price: this.price,
                    type: this.type,
                    description: this.description,
                    expirationDate: this.expirationDate
                })
            });
            const data = await response.json();
            if (response.ok) {
                alert(data.message);
                // Optionally, redirect to the product list page
                window.location.href = '/products';
            } else {
                alert('Error creating product: ' + data.error);
            }
        }
    };
}