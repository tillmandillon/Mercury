function register_user(usernameID, passwordID, emailID) {
		var formData = new FormData();
		formData.append('username', document.getElementById(usernameID).value);
		formData.append('password', document.getElementById(passwordID).value);
		formData.append('email', document.getElementById(emailID).value);
		var endpoint = '/users';
		alert(document.getElementById(passwordID).value);
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