# python_kivy

## Instalación

Crear y activar el entorno virtual:
```bash
python -m venv venv
source venv/Scripts/activate
```

Instalación de Kivy y ejemplos:
```bash
python -m pip install "kivy[base]" kivy_examples
```

## Generar requirements.txt

```bash
pip freeze > requirements.txt
```

## Verificar instalación de Kivy

```bash
python - <<EOF
import kivy
print(kivy.__version__)
EOF
```
