const { ipcRenderer } = require("electron");

function searchWindow() {
    ipcRenderer.send("openSearch")
}