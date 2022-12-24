import { Router } from "express";
import { devolverImagen, eliminarImagen, subirImagen, subirImagenCloudinary } from "../controllers/imagenController.js";
import Multer from "multer";

// es un middlewarw que agarra y vera si hay archivos y si los hay los agregara al req.file o ereq.files
const multer = Multer({
    storage: Multer.diskStorage({
        destination:(req, file, cb) => {
            console.log(file);
            cb(null, "./imagenes");
        },
        filename: (req, file, cb)=> {
            const horaActual = new Date().getTime();
            cb(null, `${horaActual}-${file.originalname}`);
        },
    }),
    limits: {
        // sirve para indicar el tamaño maximo de los archivos
        // 1 byte * 1024 = 1 kilobyte * 1024 = 1 megabyte (Mb) * 1024 = 1 Gigabyte (Gb)
        fileSize: 5 * 1024 * 1024,
    },
});

export const imagenRouter = Router();

// single() acepta un solo archivo con el nombre de la llave comoo parametro
// array(nombre) acepta un array de archivos (osea varios) mediante el nombre de la llave y en ste caso se guardara en req.files en todos los demas casos se guardara en req.file
// fields(nombre) acepta  una mezcla de archivos especificados por las llaves y se le puede colocar cuantos archivos como maximo me puede enviar
// imagenRouter.post(
//    "/subir-imagen",
//    multer.fields([
//        {name: Image, maxCount(5),}
//    ]),

imagenRouter.post("/subir-imagen", multer.single("imagen"), subirImagen);

imagenRouter.get("/devolver-imagen", devolverImagen);

imagenRouter.delete("/eliminar-imagen", eliminarImagen);

imagenRouter.post("/subir-imagen-cd", multer.single("imagen"), subirImagenCloudinary);