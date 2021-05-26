function getCookies(cookie) {
    let cookieArray = cookie.split(';');
    let cookieObject = {};
    for (let keyValue of cookieArray) {
        let KeyValueArray = keyValue.trim().split('=');
        cookieObject[KeyValueArray[0]] = KeyValueArray[1];
    }
    return cookieObject;
}
