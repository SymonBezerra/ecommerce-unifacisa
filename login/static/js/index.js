function loginForm() {
    return {
        username: '',
        password: '',
        submitLogin: async function () {
            console.log("Submitting login form with username:", this.username);
        }
    };
}