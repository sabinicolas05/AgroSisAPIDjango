from apps.Inventario.models.Insumo import *


const socketInsumos = new WebSocket("http://127.0.0.1:8000/api/insumos/");

socketInsumos.onopen = function () {
    socket.send(JSON.stringify({ message: "Insumo por acabarsr{nombre(insumo)}!" }));
};

socketInsumos.onmessage = function (events) {
    console.log("Mensaje recibido:", event.data);
};