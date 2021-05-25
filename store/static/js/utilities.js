function getCookies(cookie) {
    let cookieArray = cookie.split(';');
    let cookieObject = {};
    for (let keyValue of cookieArray) {
        let trimmedKeyValue = keyValue.trim().split('=');
        cookieObject[trimmedKeyValue[0]] = trimmedKeyValue[1];
    }
    return cookieObject;
}
