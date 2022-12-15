import { Usuario } from "../models/usuarioModel.js";
import bcryptjs from "bcryptjs";

export async function registro(req, res) {
    const data = req.body;
    console.log(data)

    try {
        const password = bcryptjs.hashSync(data.password, 10); // 10es el ciclo de veces para construir la contraseña
        const nuevoUsuario = await Usuario.create({ ...data, password}); // ... saca el contenido de un json de la data y modifica una elemento
        console.log(nuevoUsuario);

        res.status(201).json({
            message: "Usuario creado exitosamente",
        });
    } catch (error) {
        res.status(500).json({
            message: "Error al crear el usuario",
            content: error.message,
        });
    }
}

export async function login(req, res) {
    const data = req.body;
    const usuarioEncontrado = await Usuario.findOne({email: data.email});
    console.log(usuarioEncontrado);
    if(!usuarioEncontrado){
        return res.status(404).json({
            message:"El usuario no existe",
        });
    }
    if (bcryptjs.compareSync(data.password, usuarioEncontrado.password)) {
        res.json({
            message: "Bienvenido",
        });
    } else {
        res.json({
            message: "Error al ingresar, la contraseña no es valida",
        });
    }
}