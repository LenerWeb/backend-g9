import { Router } from "express";
import { login, registro } from "../controllers/usuarioController.js";

export const usuarioRouter = Router();

usuarioRouter.post("/Registro", registro);
usuarioRouter.post("/login", login);