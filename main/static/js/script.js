let input = document.getElementById("inputTag");

input.addEventListener("change", () => {
	let imageName = document.getElementById("imageName");
	imageName.innerText = input.files[0].name;
})