import jsonwebtoken from "jsonwebtoken";
import { Usuario } from "../models/usuarioModel.js";
// Middleware => es un controlador intermedio que se encarga de validar que la operacion se realice correctamente, si algo esta mal o invalido lo detendra y no permitira que pase al siguiente controlador (el siguiente controlador puede ser otro middleware o el controlador final)

export async function vigilante(req, res, next){
    console.log('Yo soy un middleware');
    
    // primero verificamos que tengamos un token
    // headers cabecera de la token es ahi donde se encia el user-agent (host o servidores), host (host del cliente)
    if(!req.headers.authorization){
        return res.status(401).json({
            message: "Se necesita una token para esta operacion",
        })
    }
    const token = req.headers.authorization.split(" ")[1];
    console.log(token);
    try {
        const resultado = jsonwebtoken.verify(token, process.env.JWT_SECRET);
        console.log(resultado)
        // buscaremos a ese usuario
        const usuarioEncontrado = await Usuario.findById(resultado.jti);

        //si no existe el usuario encontrado emitimos un erros que ingresara al catch
        if(!usuarioEncontrado) {
            throw new Error("Usuario no existe");
        }

        // agregar ese usuario al req.user para que pueda ser utilizado luego
        req.user= usuarioEncontrado.toJSON();

         // NEXT si no le pasamos nuingun parametro entonces dejara pasar, caso contrario detendra el coclo y hasta ahi no mas llegara 
        next();
    } catch (error) {
        return res.status(400).json({
            message: "Token invalida",
            content: error.message,
        });
    }
}
