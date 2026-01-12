#!/bin/bash

# Ajusta la ruta para que sea el contenedor de AMBOS repositorios
BASE_DIR="/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science"
DATE=$(date +%Y-%m-%d)

echo "🚀 Iniciando actualización: $DATE"
echo "----------------------------------------"

actualizar_repo() {
    local repo_path=$1
    echo "📦 Procesando: $(basename "$repo_path")"
    cd "$repo_path" || return

    # Configuración de seguridad para evitar errores de fin de línea (LF/CRLF)
    git config core.autocrlf true

    git add .

    if git diff-index --quiet HEAD --; then
        echo "✅ Sin cambios pendientes."
    else
        git commit -m "Actualización diaria $DATE"
        
        # Intentamos subir a la rama main (que es la que usas en GitHub)
        if git push origin main; then
            echo "🚀 Subido con éxito a GitHub."
        else
            echo "❌ Error: ¿Has hecho el 'git remote add origin'?"
        fi
    fi
    echo "----------------------------------------"
}

# Busca carpetas que contengan un .git (repositorios reales)
find "$BASE_DIR" -maxdepth 2 -name ".git" | while read -r line; do
    actualizar_repo "$(dirname "$line")"
done

echo "🏁 Proceso finalizado"