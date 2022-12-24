import express from "express";
import mongoose from "mongoose";
import { usuarioRouter } from "./routes/usuarioRoute.js";
import { agendaRouter } from "./routes/agendaRoute.js";
import { imagenRouter } from "./routes/imagenRoute.js";

const server = express();
const PORT = process.env.PORT ?? 5000;

// aca indicamos que la aplicacion entendera los json provenientes del cliente
server.use(express.json());

//indicamos que usamos un conjunto de rutas
server.use(usuarioRouter);
server.use(agendaRouter);
server.use(imagenRouter);

server.listen(PORT, async () => {
	console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
	try {
		mongoose.set("strictQuery", false);
		await mongoose.connect(process.env.MONGO_URI, {});
		console.log("Conexion exitosa a la bd");
	} catch (error) {
		console.log(error)
		console.log("Error al conectar a la base de datos");
	}
});