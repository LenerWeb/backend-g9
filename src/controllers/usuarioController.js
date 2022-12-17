import { Usuario } from "../models/usuarioModel.js";
import bcryptjs from "bcryptjs";
import jwt  from "jsonwebtoken";

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
        //es la contraseña del usuario
        const payload = {
            jti: usuarioEncontrado._id,
            nombre: usuarioEncontrado.nombre,
        };

        const token = jwt.sign(payload, process.env.JWT_SECRET, { 
            expiresIn: "1h"
        });

        res.json({
            message: "Bienvenido",
            content: token,
        });
    } else {
        res.json({
            message: "Error al ingresar, la contraseña no es valida",
        });
    }
}

export async function perfil(req, res){
    console.log(req.user);
    // seleccionamos solamente el nombre del usuario indicando las columnas separadas po eespacio y la que no se coloca un signo negativo (-)
    // const usuarioEncontrado = await Usuario.findById(req.user._id).select(
    //     "nombre email direcciones" // -_id
    //     ); 

    await Usuario.aggregate([
    
    ]).lookup({
        from: "agendas",
        localField: "agendas",
        foreignField: "_id",
        as: "agendas",
    })
    .match({ _id: req.user._id }) // es igual a { $match: {_id: req.user._id} }, encima lookup
    .project("-password");

    res.json({
        content: usuarioEncontrado,
    });
}