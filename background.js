chrome.action.onClicked.addListener((tab) => {
  chrome.proxy.settings.set({
    value: {
      mode: "fixed_servers",
      rules: {
        singleProxy: {
          scheme: "http",
          host: "192.168.1.12",
          port: 49152
        },
        bypassList: ["<local>"]
      }
    },
    scope: "regular"
  });
});
