import { Router } from "express";
import { login, perfil, registro } from "../controllers/usuarioController.js";
import { vigilante } from "../utils/wachiman.js";
export const usuarioRouter = Router();

usuarioRouter.post("/Registro", registro);
usuarioRouter.post("/login", login);
usuarioRouter.get("/perfil", vigilante, perfil);
