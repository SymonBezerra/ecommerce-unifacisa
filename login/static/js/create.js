function registerForm() {
    return {
        username: '',
        password: '',
        confirmPassword: '',
        errorMsg: '',
        submitRegister: async function () {
            const response = await fetch('/login/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: this.username,
                    password: this.password,
                    confirmPassword: this.confirmPassword
                })
            });
            const data = await response.json();
            if (!response.ok) {
                this.errorMsg = data.error || 'An error occurred during registration.';
            } else {
                alert(data.message || 'Registration successful! Please log in.');
                window.location.href = '/login';
            }
        }
    };
}