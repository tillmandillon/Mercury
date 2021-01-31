function SignUp(usernameID, passwordID, emailID) {
		var formData = new FormData();
		formData.append('username', document.getElementById(usernameID);
		formData.append('password', document.getElementById(passwordID);
		formData.append('email', document.getElementById(emailID);
		var endpoint = '/add_user';
		
		$.ajax({
			type: 'POST',
			url: endpoint,
			data: formData,
			contentType: false,
			cache: false,
			processData: false,
			success: function(data) {
				swal("Successfully registered!");
			}
		});
}