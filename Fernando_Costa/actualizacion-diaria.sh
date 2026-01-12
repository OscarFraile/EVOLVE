#!/bin/bash

# 1. Ajuste de la ruta base (Basado en tu captura)
# Asegúrate de que esta ruta sea la carpeta que contiene "EVOLVE" y "evolve-data-python"
BASE_DIR="/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science/EVOLVE"
DATE=$(date +%Y-%m-%d)

echo "🚀 Iniciando actualización: $DATE"
echo "----------------------------------------"

# 2. Función para procesar cada repo
actualizar_repo() {
    local repo_path=$1
    if [ -d "$repo_path/.git" ]; then
        echo "📦 Procesando: $(basename "$repo_path")"
        cd "$repo_path" || return

        # Añadir cambios (excluyendo lo que esté en .gitignore)
        git add .

        # Verificar si hay algo que enviar
        if git diff-index --quiet HEAD --; then
            echo "✅ Sin cambios pendientes."
        else
            git commit -m "Actualización diaria de notebooks y ejercicios personales $DATE"
            
            # Intentar subir a la rama 'main' o 'master'
            if git push origin main; then
                echo "🚀 Subido a main."
            elif git push origin master; then
                echo "🚀 Subido a master."
            else
                echo "❌ Error al subir cambios."
            fi
        fi
        echo "----------------------------------------"
    fi
}

# 3. Ejecución: Buscamos repositorios en el nivel actual y un nivel más abajo
# Esto cubrirá tanto 'EVOLVE' como 'evolve-data-python'
find "$BASE_DIR" -maxdepth 2 -name ".git" | while read -r line; do
    actualizar_repo "$(dirname "$line")"
done

echo "🏁 Proceso finalizado"