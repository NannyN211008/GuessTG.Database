const assets = [
    "/",
    "/static/css/style.css",
    "/static/js/app.js",
    "/static/images/logo.png",
    "/static/images/favicon.png",
    "/static/icons/icon-128x128.png",
    "/static/icons/icon-192x192.png",
    "/static/icons/icon-384x384.png",
    "/static/icons/icon-512x512.png",
    "/static/icons/desktop_screenshot.png",
    "/static/icons/mobile_screenshot.png",
];

const CACHE_NAME = "catalogue-assets";

self.addEventListener("install", (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            console.log("Caching files...");
            return cache.addAll(assets);
        }).then(() => self.skipWaiting())
    );
});

self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys.map((key) => {
                    if (key !== CACHE_NAME) {
                        return caches.delete(key);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

self.addEventListener("fetch", (event) => {
    event.respondWith(
        fetch(event.request).catch(() => {
            return caches.match(event.request);
        })
    );
});