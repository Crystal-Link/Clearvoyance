document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('#submitImg');
    button.onclick = () => {
        const request = new XMLHttpRequest();
        request.open('POST', '/handle-click');
        request.onload = () => {
            const data = request.responseText;
            console.log(data);
        };
        request.send();
    };
});
