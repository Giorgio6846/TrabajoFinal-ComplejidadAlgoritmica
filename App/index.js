const { app, BrowserWindow, Menu, ipcMain } = require("electron");
const url = require("url");

childClosed = true

function mainWindow() {
    mainWin = new BrowserWindow({
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
        },
    });
        
    mainWin.loadFile("index.html");


    mainWin.webContents.openDevTools();
}

const mainMenu = [
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
/*
function crearHijo(){
    childWin = new BrowserWindow({
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
        },
    });

    childWin.loadURL(
        url.format({
            pathname: "src/search/search.html",
            slashes: true
        })
    );
}

ipcMain.on("openSearch", (event,data) => {
    console.log(childClosed)

    if(childClosed)
    {
        childClosed = false

        childWin.show()
        childWin.webContents.openDevTools();
    }
})
*/
const menu = Menu.buildFromTemplate(mainMenu)
Menu.setApplicationMenu(menu)
app.on("ready", () => {
    mainWindow()
    /*crearHijo()

    childWin.on('close',function(e){
        childWin.hide()  
        childClosed = true
    });
    */
});