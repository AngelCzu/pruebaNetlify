var interfaceConfig = {

    TOOLBAR_BUTTONS: [
        'microphone',
        'camera',
        'desktop',
        'fullscreen',
        'fodeviceselection',
        'hangup', // Botón para salir
        'videoquality',
        'tileview',
        'e2ee'
    ],

    SETTINGS_SECTIONS: [
        'devices',
        'language',
        'moderator',
        'profile',
        // 'calendar'
    ],
    SHOW_CHROME_EXTENSION_BANNER: false
};

const domain = 'meet.jit.si';

const options = {
    roomName: 'Stream',
    width: '100%',
    height: 500,
    parentNode: document.querySelector('#meet'),
    userInfo: {
        email: "admin@gmail.com",
        displayName: "PROFESOR CLASES YA",
    },
    noSsl: true,
    interfaceConfigOverwrite: interfaceConfig,
};
const api = new JitsiMeetExternalAPI(domain, options);

function cerrarSala() {
    api.dispose();
}
