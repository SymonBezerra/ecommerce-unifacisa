function listProducts() {
    return {
        deleteProduct: function (productId) {
            if (confirm("Are you sure you want to delete this product?")) {
                fetch(`/products/delete/${productId}`, {
                    method: "DELETE",
                })
                    .then((response) => {
                        if (response.ok) {
                            alert("Product deleted successfully!");
                            location.reload();
                        } else {
                            alert("Failed to delete the product.");
                        }
                    })
                    .catch((error) => {
                        console.error("Error:", error);
                        alert("An error occurred while deleting the product.");
                    });
            }
        }
    }
}