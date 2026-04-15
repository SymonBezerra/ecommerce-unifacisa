function loginForm() {
    return {
        username: '',
        password: '',
        errorMsg: '',
        submitLogin: async function () {
            const response = await fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: this.username,
                    password: this.password
                })
            });
            const data = await response.json();
            if (!response.ok) {
                this.errorMsg = data.error || 'An error occurred during login.';
            } else {
                alert(data.message || 'Login successful!');
                window.location.href = '/';
            }
        }
    };
}