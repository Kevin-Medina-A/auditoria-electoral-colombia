# src/utils_styles.py
from IPython.display import HTML, display

def obtener_config_tabla():
    """Retorna las estructuras CSS base para las tablas del notebook."""
    estilo_base = [
        {
            'selector': 'th', 
            'props': [
                ('background-color', '#2d2d2d'), 
                ('color', '#ffffff'), 
                ('border', '1px solid #555555'), 
                ('text-align', 'center'),
                ('font-weight', 'bold'),
                ('padding', '10px')
            ]
        },
        {
            'selector': 'table', 
            'props': [
                ('border-collapse', 'collapse'), 
                ('width', '100%'),
                ('background-color', '#111111'),
                ('margin-bottom', '25px')
            ]
        }
    ]
    
    propiedades_celdas = {
        'border': '1px solid #555555',
        'text-align': 'center',
        'padding': '8px',
        'color': '#ffffff'
    }
    
    return estilo_base, propiedades_celdas


def renderizar_tabla_estilizada(df_style, titulo=""):
    """Aplica los estilos cargados y despliega la tabla como HTML limpio."""
    estilo_base, propiedades_celdas = obtener_config_tabla()
    
    tabla_final = (
        df_style
        .set_properties(**propiedades_celdas)
        .set_table_styles(estilo_base)
        .hide(axis='index')
    )
    
    if titulo:
        print(titulo)
    display(HTML(tabla_final.to_html()))