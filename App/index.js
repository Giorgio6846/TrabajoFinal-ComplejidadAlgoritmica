const { app, BrowserWindow, Menu, MenuItem, ipcMain, ipcRenderer } = require("electron");

const url = require("url");
const { markAsUntransferable } = require("worker_threads");

function mainWindow() {
    mainWin = new BrowserWindow();
    
    
    mainWin.loadURL(
        url.format({
            pathname: "index.html",
            slashes: true
        })
    );
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
    /*{
        label: 'Search',
        submenu: [
            {
                label: 'Open Window',
                click() {
                    alert("OwO");
                }
            }
        ]
    }*/
]

function searchWindow(){
    ipcRenderer.send("openSearch")
}

ipcMain.on("openSearch", (event,data) => {
    let childWin = new BrowserWindow();

    childWin.loadURL(
        url.format({
            pathname: "search.html",
            slashes: true
        })
    );
    childWin.show()

})

const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)
app.on("ready", mainWindow);