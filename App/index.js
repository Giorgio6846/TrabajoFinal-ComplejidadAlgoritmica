const { app, BrowserWindow, Menu, MenuItem } = require("electron");

const url = require("url");
const { markAsUntransferable } = require("worker_threads");

function mainWindow() {
    win = new BrowserWindow();
    
    win.loadURL(
        url.format({
            pathname: "index.html",
            slashes: true
        })
    );
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

const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)
app.on("ready", mainWindow);