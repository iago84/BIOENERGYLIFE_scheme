import ast
import os

def comentar_funcion(func):
    """Devuelve un string con el comentario de la función según su nombre y argumentos."""
    args = [arg.arg for arg in func.args.args]
    return f"    # Función: {func.name}({', '.join(args)})\n" \
           f"    # Descripción: {func.name.replace('_', ' ').capitalize()}."

def comentar_clase(cls):
    """Devuelve un string con el comentario de la clase."""
    return f"# Clase: {cls.name}\n# Descripción: Modelo de {cls.name.lower()}.\n"

def documentar_archivo(file_path):
    """Genera un bloque de documentación en Markdown del archivo analizado."""
    with open(file_path, 'r', encoding='utf-8') as f:
        source = f.read()
    tree = ast.parse(source, filename=file_path)

    doc_md = []
    doc_md.append(f"# Documentación de `{os.path.basename(file_path)}`\n")
    doc_md.append("---\n")
    if tree.body and isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Str):
        doc_md.append(f"**Descripción:** {tree.body[0].value.s}\n")
    doc_md.append("## Funciones principales\n")
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            args = [arg.arg for arg in node.args.args]
            doc_md.append(f"- **{node.name}({', '.join(args)})**: {node.name.replace('_', ' ').capitalize()}.")
        elif isinstance(node, ast.ClassDef):
            doc_md.append(f"\n### Clase: `{node.name}`\n")
            doc_md.append("#### Métodos:\n")
            for n2 in node.body:
                if isinstance(n2, ast.FunctionDef):
                    args = [arg.arg for arg in n2.args.args]
                    doc_md.append(f"  - **{n2.name}({', '.join(args)})**")
    return '\n'.join(doc_md)

def comentar_y_documentar(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tree = ast.parse(''.join(lines), filename=file_path)
    # Insertamos comentarios antes de cada función o clase
    new_lines = []
    last_pos = 0
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            comentario = comentar_funcion(node)
            new_lines.append('\n' + comentario)
        elif isinstance(node, ast.ClassDef):
            comentario = comentar_clase(node)
            new_lines.append('\n' + comentario)
        # Copia línea original (la función o clase se añade luego)
        start = node.lineno - 1
        for i in range(last_pos, start):
            new_lines.append(lines[i])
        new_lines.append(lines[start])
        last_pos = start + 1

    for i in range(last_pos, len(lines)):
        new_lines.append(lines[i])

    # Guardar archivo comentado
    file_base = os.path.splitext(file_path)[0]
    comentado_path = f"{file_base}_comentado.py"
    with open(comentado_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    # Generar documentación markdown
    doc_md = documentar_archivo(file_path)
    doc_path = f"{file_base}_doc.md"
    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(doc_md)

    print(f"Archivo comentado: {comentado_path}")
    print(f"Documentación Markdown: {doc_path}")

# === USO ===
# Comenta y documenta cualquier archivo .py que le pases:
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python comenta_y_documenta.py <archivo1.py> [<archivo2.py> ...]")
    else:
        for fpath in sys.argv[1:]:
            comentar_y_documentar(fpath)
