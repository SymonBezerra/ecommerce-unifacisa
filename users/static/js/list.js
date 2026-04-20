function listUsers() {
    return {
        deleteUser(userId) {
            if (confirm('Are you sure you want to delete this user?')) {
                fetch(`/users/delete/${userId}`, {
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