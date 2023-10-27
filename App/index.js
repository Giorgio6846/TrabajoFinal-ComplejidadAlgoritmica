const { app, BrowserWindow, Menu, ipcMain } = require("electron");

const url = require("url");
const { markAsUntransferable } = require("worker_threads");

function mainWindow() {
    mainWin = new BrowserWindow({
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
        },
    });
        
    mainWin.loadFile("index.html");

    /*
        mainWin.loadURL(
        url.format({
            pathname: "index.html",
            slashes: true
        })
    );
    */

    mainWin.webContents.openDevTools();
}

const template = [
    {
        label: 'Dev',
        submenu: [
            {
                role: 'toggledevtools'
            },
            {
                role: 'reload'
            },
            {
                role: 'forcereload'
            }
        ],
    },
]

ipcMain.on("openSearch", (event,data) => {
    let childWin = new BrowserWindow();

    childWin.loadURL(
        url.format({
            pathname: "src/search/search.html",
            slashes: true
        })
    );

    childWin.show()
})

const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)
app.on("ready", mainWindow);