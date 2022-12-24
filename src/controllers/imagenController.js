import path from "path";
import fs from "fs";
import { v2 } from "cloudinary";

v2.config({
    cloud_name: 'duphajs70', 
    api_key: '227123777471844', 
    api_secret: 'VDGft6p5ZV2TYjeKhV9T8lgSNlQ'
});

export async function subirImagen(req, res){
    console.log(req.file);
    res.json({
        message: "imagen subida exitosamente"
    });
}

export async function devolverImagen(req, res) {
    // query params http://localhost;5000/devolver-imagen$nombre
    const { nombre, extension } = req.query;

    // devolvera la ubicacion de nuestro archivo package.json dentro del servidor o maquina
    const __dirname = path.resolve();
    console.log(__dirname)
    const nombreCompleto = `${nombre}.${extension}`;
    
    // el metodo join sirve para colocar la ubicacion que queremos  el se encargara de colocar el '/' o el '\' dependiendo del sistema operativo
    const rutaArchivo = path.join(__dirname, "imagenes", nombreCompleto);
    console.log(rutaArchivo);

    try {
        fs.readFileSync(rutaArchivo);

        res.sendFile(rutaArchivo);
    } catch (error) {
        res.status(404).json({
            message: "Archivo no existe"
        });
    }
}

export function eliminarImagen(req, res) {
    const { nombre, extension } = req.query;

    const __dirname = path.resolve();
    const nombreCompleto = `${nombre}.${extension}`;
    const rutaArchivo = path.join(__dirname, "imagenes", nombreCompleto);

    try {
        fs.unlinkSync(rutaArchivo);
        res.json({
            message: "Imagen eliminada exitosamente"
        });
    } catch (error) {
        res.status(404).json({
            message: "Archivo no existe"
        })
    }
}

//-----------------------CON CLOUDINARY-----------------------------------

export async function subirImagenCloudinary(req, res) {
    const archivo = req.file;
    const resultado = await v2.uploader.upload(archivo, {folder:"pruebas"});
    console.log(resultado);

    res.json({
        message: "Archivo subido exitosamente",
    });
}


