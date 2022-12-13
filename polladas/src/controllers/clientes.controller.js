import { Prisma } from "../prisma";

export const crearCliente = async(req, res)=>{
    const data = req.body
    try {
        const cliente = await Prisma.cliente.create({
            data,
        });
        return res.status(201).json({
            message: "Cliente creado",
            content: cliente,
        })
    } catch (error) {
        return res.status(500).json({
            message: "Error en el servidor",
            error: error.message,
        });
    }
};