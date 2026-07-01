import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os
import requests
import time
from datetime import datetime

# ==========================================
# 1. CONFIGURACIÓN VISUAL Y ESTÉTICA PREMIUM (VERDE AMBIENTAL MODERNO)
# ==========================================
st.set_page_config(page_title="Bioterra - Gestión Minera", layout="wide", page_icon="⛏️")

st.markdown("""
    <style>
        /* Fondo global de la aplicación */
        .stApp { 
            background-color: #F8F9FA; 
        }
        
        /* Banner de Encabezado Corporativo */
        .header-container {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 8px;
            border-bottom: 4px solid #285A48;
            margin-bottom: 25px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        }
        .header-title {
            color: #285A48 !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 32px;
            font-weight: 800;
            margin: 0;
            letter-spacing: -0.5px;
        }
        .header-subtitle {
            color: #6C757D;
            font-size: 14px;
            margin-top: 5px;
            margin-bottom: 0;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Títulos y Subtítulos estándar en los módulos */
        h1, h2, h3, h4 { 
            color: #285A48 !important; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        
        /* Estilizado de las Pestañas (Tabs) */
        .stTabs [data-baseweb="tab"] { 
            color: #6C757D; 
            font-weight: 600; 
            font-size: 15px;
            padding: 10px 20px;
        }
        .stTabs [aria-selected="true"] { 
            color: #285A48 !important; 
            border-bottom: 3px solid #285A48 !important; 
        }
        
        /* Botones Principales en Verde Esmeralda Oscuro */
        div.stButton > button:first-child { 
            background-color: #285A48; 
            color: white; 
            border-radius: 8px; 
            border: none;
            padding: 10px 24px;
            font-weight: 600;
            box-shadow: 0 2px 4px rgba(40, 90, 72, 0.2);
            transition: all 0.3s ease;
        }
        
        div.stButton > button:first-child:hover { 
            background-color: #34745D; 
            color: white;
            box-shadow: 0 4px 8px rgba(40, 90, 72, 0.3);
            transform: translateY(-1px);
        }
        
        /* Contenedor tipo Tarjeta para formularios y secciones */
        .card-panel {
            background-color: #FFFFFF; 
            border-left: 6px solid #285A48; 
            padding: 20px; 
            margin: 15px 0; 
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }
        
        /* Estilo para las métricas numéricas (KPIs) en Verde */
        [data-testid="stMetricValue"] {
            color: #285A48 !important;
            font-weight: 700;
        }
        
        /* Pie de página corporativo */
        .footer {
            position: fixed; 
            left: 0; 
            bottom: 0; 
            width: 100%; 
            background-color: #FFFFFF; 
            color: #285A48;
            text-align: center; 
            padding: 12px 0; 
            font-weight: 600; 
            font-size: 13px; 
            border-top: 1px solid #E9ECEF; 
            box-shadow: 0 -2px 10px rgba(0,0,0,0.03);
            z-index: 100;
        }
            /* Configuración estética del menú lateral (Sidebar) */
        [data-testid="stSidebar"] {
            background-color: #285A48 !important;
        }
        
        /* Cambiar el color del texto y etiquetas dentro del menú a blanco para el contraste */
        [data-testid="stSidebar"] section, 
        [data-testid="stSidebar"] .stMarkdown, 
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] p {
            color: #FFFFFF !important;
        }

        /* Cambiar el color de los elementos de selección (radio buttons/selectboxes) dentro del menú */
        [data-testid="stSidebar"] div[role="radiogroup"] label {
            color: #FFFFFF !important;
            background-color: rgba(255, 255, 255, 0.05);
            padding: 8px 12px;
            border-radius: 6px;
            margin-bottom: 4px;
            transition: background 0.2s ease;
        }

        /* Efecto al pasar el mouse sobre las opciones del menú lateral */
        [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background-color: rgba(255, 255, 255, 0.15) !important;
            cursor: pointer;
        }

        /* Color de la flecha que expande y contrae el menú */
        [data-testid="stSidebarCollapseButton"] button {
            color: #285A48 !important; /* Si está afuera en el fondo claro */
        }
        [data-testid="stSidebar"] button {
            color: #FFFFFF !important; /* Si está adentro en el fondo verde */
        }
            
         
        

    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🏢 BANNER DE ENCABEZADO VISIBLE
# ==========================================
st.markdown("""
    <div class="header-container">
        <div class="header-title">🌱 Bioterra Consulting S.A.C.</div>
        <div class="header-subtitle">Sistema Integrado de Gestión Ambiental y Catastro Minero</div>
    </div>
""", unsafe_allow_html=True)






# Pega aquí el enlace largo que te dio Google Apps Script en el Paso 1
URL_API = "https://script.google.com/macros/s/AKfycbxIIymwlHm9eKzFOghFkxPZlLx62wkt6zelbVNw1Xjnd6X4k8ws3HaBJJqvCqaRCyyQ/exec"

# Tu link público para leer (el que ya funcionaba)
LINK_PUBLICO = "https://docs.google.com/spreadsheets/d/1NeTtK_O9MSVxttpuDZmPBLVmWsm95GGv/edit?gid=2131864427#gid=2131864427"

def obtener_url_pestana(link_base, nombre_pestana):
    id_sheet = link_base.split("/d/")[1].split("/")[0]
    # Este enlace limpio jala el CSV directo de Google
    return f"https://docs.google.com/spreadsheets/d/{id_sheet}/gviz/tq?tqx=out:csv&sheet={nombre_pestana}"



# ---- TU FUNCIÓN DE CARGA (Actualizada para la nube) ----
def cargar_datos(pestana):
    try:
        # Llamamos a tu API de Google pasándole el nombre de la pestaña
        respuesta = requests.get(f"{URL_API}?pestana={pestana}")
        datos_json = respuesta.json()
        
        # Si está vacío, genera el DataFrame vacío base
        if not datos_json:
            raise Exception("Pestaña vacía")
            
        return pd.DataFrame(datos_json)
        
    except Exception:
        columnas_base = {
            "Administrados": ["ID_Administrado", "RUC_DNI", "Razon_Social", "Tipo_Persona", "Condicion", "Fecha_Registro"],
            "Petitorios_Concesiones": ["ID_Derecho", "Codigo_Unico", "Nombre_Derecho", "ID_Administrado", "Sustancia", "Hectareas", "Estado_Fase", "Fecha_Formulacion"]
        }
        return pd.DataFrame(columns=columnas_base.get(pestana, []))
    
    

    
# ---- TU FUNCIÓN DE GUARDADO (¡Adaptada a tu API gratis!) ----
def guardar_datos(df_nuevo, pestana):
    try:
        # Volvemos a tu lógica original que funcionaba perfecto y no rompía nada
        df_limpio = df_nuevo.fillna("")
        datos_json = df_limpio.to_dict(orient="records")
        payload = {"pestana": pestana, "datos": datos_json}
        
        respuesta = requests.post(URL_API, json=payload)
        
        if respuesta.text == "Éxito":
            st.success(f"¡Datos guardados con éxito en la pestaña {pestana}!")
            
            # ⬇️ LA SOLUCIÓN AQUÍ ⬇️
            # Borramos la memoria interna de Streamlit para que no use datos viejos
            st.cache_data.clear()
            
            # Forzamos a la página a reiniciarse y volver a leer el Excel actualizado
           
        else:
            st.error("El servidor de Google no respondió correctamente.")
    except Exception as e:
        st.error(f"Error al guardar: {e}")




# ---- Carga masiva ----
df_administrados = cargar_datos("Administrados")
df_concesiones = cargar_datos("Petitorios_Concesiones")
df_calificaciones = cargar_datos("Calificaciones_Mineras")
df_vigencias = cargar_datos("Control_Vigencias")
df_seguimiento = cargar_datos("Seguimiento_Tramites")

# ---- INTERFAZ DE STREAMLIT ----
#st.title("Sistema de Petitorios Mineros (Vista Previa)")

# Mostrar pestañas en Streamlit para revisar que todo cargó bien
#tab1, tab2, tab3 = st.tabs(["Administrados", "Petitorios y Concesiones", "Control de Vigencias"])

#with tab1:
    #st.subheader("Datos de Administrados")
    #st.dataframe(df_administrados)

#with tab2:
    #st.subheader("Petitorios y Concesiones")
    #st.dataframe(df_concesiones)

#with tab3:
   # st.subheader("Control de Vigencias")
 #   st.dataframe(df_vigencias)




# ---- INTERFAZ PRINCIPAL ----
st.title("⛏️ Sistema de Catastro y Control de Obligaciones Mineras")
st.markdown("<p style='color: #555555;'>Consola interna de análisis y consistencia jurídica ambiental — BIOTERRA</p>", unsafe_allow_html=True)

menu = st.sidebar.selectbox(
    "Seleccione Módulo de Trabajo",
    [
        "🏠 Dashboard de Concesiones", 
        "👥 Calificaciones y Límites", 
        "📝 Registro de Datos", 
        "📋 Seguimiento de Trámites", 
        "💰 Control de Pagos / Vigencia",
        "👤 Análisis por Administrados" ,
         "🔧 Actualización de Datos" # <-- Agregamos la nueva opción aquí
    ]
)

# ==========================================
# MÓDULO 1: DASHBOARD GENERAL
# ==========================================
if menu == "🏠 Dashboard de Concesiones":
    st.subheader("Estado General del Catastro Local")
    col1, col2, col3 = st.columns(3)
    col1.metric("Administrados Registrados", len(df_administrados))
    col2.metric("Total Derechos Ocupados", len(df_concesiones))
    pendientes = len(df_vigencias[df_vigencias['Estado_Pago'] == 'Pendiente']) if not df_vigencias.empty else 0
    col3.metric("Obligaciones Financieras Pendientes", pendientes)
    
    st.markdown("### 📋 Vista de Derechos Mineros Cargados")
    if not df_concesiones.empty:
        st.dataframe(df_concesiones, use_container_width=True)
    else:
        st.info("No se registran petitorios vigentes en el archivo Excel actual.")

# ==========================================
# MÓDULO 2: CALIFICACIONES Y LÍMITES
# ==========================================
elif menu == "👥 Calificaciones y Límites":
    st.subheader("Análisis Dinámico de Calificaciones de Productores")
    if not df_administrados.empty and "Razon_Social" in df_administrados.columns:
        busqueda = st.selectbox("Seleccione un Administrado para evaluar:", df_administrados["Razon_Social"].unique())
        id_adm = df_administrados[df_administrados["Razon_Social"] == busqueda]["ID_Administrado"].values[0]
        
        calif_adm = df_calificaciones[df_calificaciones["ID_Administrado"] == id_adm] if not df_calificaciones.empty else pd.DataFrame()
        concesiones_adm = df_concesiones[df_concesiones["ID_Administrado"] == id_adm] if not df_concesiones.empty else pd.DataFrame()
        
        col_c1, col_c2 = st.columns(2)


        # Línea 317: Va pegada a la izquierda del bloque actual
    with col_c1:
        # Línea 318 en adelante: TODO lleva un paso de sangría (Tabulador) hacia la derecha
        st.markdown("#### 🕒 Estado de la Calificación Minera")
        if not calif_adm.empty and "Fecha_Emision_Constancia" in calif_adm.columns and pd.notna(calif_adm["Fecha_Emision_Constancia"].values[0]):
            estrato_actual = calif_adm["Estrato"].values[0]
            
            # Estas líneas llevan DOBLE paso de sangría porque están dentro del 'with' Y dentro del 'if'
            fecha_original = pd.to_datetime(str(calif_adm["Fecha_Emision_Constancia"].values[0]))
            fecha_emision = fecha_original.tz_localize(None) if fecha_original.tzinfo is not None else fecha_original
            
            dias_pasados = (datetime.now() - fecha_emision).days
            anios_pasados = dias_pasados / 365.25
            st.write(f"**Estrato de Registro:** `{estrato_actual}`")
            
            if "Régimen" in estrato_actual or "General" in estrato_actual:
                st.success("✅ **VIGENCIA PERMANENTE:** El Régimen General no requiere renovación bienal.")
            else:
                if anios_pasados > 2.0:
                    st.error(f"🚨 **CALIFICACIÓN VENCIDA:** Han transcurrido {anios_pasados:.2f} años.")
                else:
                    st.success(f"✅ **CALIFICACIÓN VIGENTE:** Vence a los 2 años. Transcurrido: {anios_pasados:.2f} años.")
        else:
            st.warning("No se registra fecha de emisión.")
                
        with col_c2:
            st.markdown("#### 📐 Consistencia de Áreas")
            if not calif_adm.empty:
                estrato_actual = calif_adm["Estrato"].values[0]
                limite_ha = calif_adm["Limite_Hectareas"].values[0]
                ha_actuales = concesiones_adm["Hectareas"].sum() if not concesiones_adm.empty else 0
                st.write(f"**Hectáreas Acumuladas:** {ha_actuales} Ha")
                
                if "Régimen" in estrato_actual or "General" in estrato_actual:
                    st.info("ℹ️ **RÉGIMEN GENERAL:** Sin límite máximo de hectáreas permitidas.")
                    st.progress(1.0)
                else:
                    st.write(f"**Límite Máximo ({estrato_actual}):** {limite_ha} Ha")
                    if ha_actuales > limite_ha:
                        st.error(f"🚨 **EXCESO DE LÍMITE:** Excede en {ha_actuales - limite_ha} Ha.")
                    else:
                        st.success("✅ **Área dentro del margen.**")
                    st.progress(min(float(ha_actuales / limite_ha), 1.0) if limite_ha > 0 else 0.0)

# ==========================================
# MÓDULO 3: REGISTRO DE DATOS 
# ==========================================
elif menu == "📝 Registro de Datos":
    st.subheader("Entrada de Nuevos Registros al Catastro")
    tab0, tab_reclass, tab1 = st.tabs(["👥 Registrar Nuevo Administrado", "🔄 Cambiar Estrato / Reclasificación", "🆕 Registrar Nuevo Petitorio"])
    
    with tab0:
        st.write("### 👤 Ficha de Inscripción de Administrado")
        id_adm_nuevo = f"ADM-{len(df_administrados) + 1:03d}" if not df_administrados.empty else "ADM-001"
        st.info(f"🔑 **Código Automático Asignado:** `{id_adm_nuevo}`")
        with st.form("form_adm"):
            ruc_dni = st.text_input("RUC o DNI:")
            razon_social = st.text_input("Razón Social / Nombre:")
            tipo_p = st.selectbox("Persona:", ["Jurídica", "Natural"])
            estrato = st.selectbox("Estrato Minero Inicial:", ["Régimen General", "PPM (Pequeño)", "PMA (Artesanal)"])
            fecha_constancia = st.date_input("Fecha de Emisión Inicial:")
            limite_sug = 1000 if "PMA" in estrato else (2000 if "PPM" in estrato else 999999)
            btn_adm = st.form_submit_button("Guardar Administrado")
            if btn_adm:
                df_administrados = pd.concat([df_administrados, pd.DataFrame([{"ID_Administrado": id_adm_nuevo, "RUC_DNI": ruc_dni, "Razon_Social": razon_social, "Tipo_Persona": tipo_p, "Condicion": "Activo", "Fecha_Registro": datetime.now().strftime("%Y-%m-%d")}])], ignore_index=True)
                guardar_datos(df_administrados, "Administrados")
                df_calificaciones = pd.concat([df_calificaciones, pd.DataFrame([{"ID_Calificacion": f"CAL-{len(df_calificaciones)+1:03d}", "ID_Administrado": id_adm_nuevo, "Estrato": estrato.split()[0], "Limite_Hectareas": limite_sug, "Fecha_Emision_Constancia": fecha_constancia.strftime("%Y-%m-%d")}])], ignore_index=True)
                guardar_datos(df_calificaciones, "Calificaciones_Mineras")
                st.success("Registrado correctamente.")

    with tab_reclass:
        st.write("### 🔄 Tramitación de Cambio de Calificación (PMA / PPM)")
        if not df_administrados.empty:
            with st.form("form_reclasificacion"):
                adm_cambio = st.selectbox("Seleccione el Administrado:", df_administrados["Razon_Social"].unique())
                nuevo_estrato = st.selectbox("Nuevo Estrato Aprobado:", ["PMA (Artesanal)", "PPM (Pequeño)", "Régimen General"])
                nro_expediente = st.text_input("Número de Expediente:")
                nro_resolucion = st.text_input("Número de Resolución Directoral (RD):")
                fecha_aprobacion = st.date_input("Fecha de Aprobación:")
                btn_reclass = st.form_submit_button("Registrar Reclasificación")
                if btn_reclass:
                    id_adm_sel = df_administrados[df_administrados["Razon_Social"] == adm_cambio]["ID_Administrado"].values[0]
                    ha_totales = df_concesiones[df_concesiones["ID_Administrado"] == id_adm_sel]["Hectareas"].sum() if not df_concesiones.empty else 0
                    
                    if "PMA" in nuevo_estrato and ha_totales > 1000:
                        st.error(f"❌ Improcedente: Posee {ha_totales} Ha. (Máx PMA: 1000 Ha)")
                    elif "PPM" in nuevo_estrato and ha_totales > 2000:
                        st.error(f"❌ Improcedente: Posee {ha_totales} Ha. (Máx PPM: 2000 Ha)")
                    else:
                        fecha_term = pd.to_datetime(fecha_aprobacion) + pd.Timedelta(days=730)
                        nuevo_lim = 1000 if "PMA" in nuevo_estrato else (2000 if "PPM" in nuevo_estrato else 999999)
                        df_calificaciones.loc[df_calificaciones["ID_Administrado"] == id_adm_sel, ["Estrato", "Limite_Hectareas", "Fecha_Emision_Constancia", "Expediente_Cambio", "Resolucion_Cambio", "Fecha_Termino_Constancia"]] = [nuevo_estrato.split()[0], nuevo_lim, fecha_aprobacion.strftime("%Y-%m-%d"), nro_expediente, nro_resolucion, fecha_term.strftime("%Y-%m-%d")]
                        guardar_datos(df_calificaciones, "Calificaciones_Mineras")
                        st.success("Reclasificación indexada en el Excel.")

    with tab1:
        st.write("### 🆕 Ingresar Nuevo Petitorio Minero")
        if not df_administrados.empty:
            with st.form("form_petitorio"):
                id_der = st.text_input("ID Interno Derecho (Ej: PET-01):")
                cod_u = st.text_input("Código Único INGEMMET:")
                nom_der = st.text_input("Nombre de la Concesión:")
                titular = st.selectbox("Titular Designado:", df_administrados["Razon_Social"].unique())
                subst = st.selectbox("Sustancia:", ["Metálica", "No Metálica"])
                ha = st.number_input("Hectareas:", min_value=1.0)
                btn_pet = st.form_submit_button("Inscribir Petitorio")
                if btn_pet:
                    id_adm_sel = df_administrados[df_administrados["Razon_Social"] == titular]["ID_Administrado"].values[0]
                    df_concesiones = pd.concat([df_concesiones, pd.DataFrame([{"ID_Derecho": id_der, "Codigo_Unico": cod_u, "Nombre_Derecho": nom_der, "ID_Administrado": id_adm_sel, "Sustancia": subst, "Hectareas": ha, "Estado_Fase": "En trámite", "Fecha_Formulacion": datetime.now().strftime("%Y-%m-%d")}])], ignore_index=True)
                    guardar_datos(df_concesiones, "Petitorios_Concesiones")
                    st.success(f"🎉 Petitorio '{nom_der}' guardado. Ahora puedes pasar al módulo de Seguimiento para cargar su expediente.")

# ==========================================
# 🚀 MÓDULO 4: HISTORIAL DE TRÁMITES CON HERENCIA ESTRICTA DE CÓDIGO (SEG-XXX)
# ==========================================
elif menu == "📋 Seguimiento de Trámites":
    st.subheader("Control de Flujos, Notificaciones y Plazos del Procedimiento Ordinario")
    
    t_ver, t_reg_oblig, t_reg_info = st.tabs([
        "📊 Panel de Control e Historial", 
        "⚠️ Registrar Obligación de Respuesta (Mismo ID)", 
        "ℹ️ Registrar Ciclo Final (Mismo ID)"
    ])
    
    # FUNCIÓN DE ORO: Garantiza que el código SEG-XXX esté amarrado de por vida a la concesión
    # FUNCIÓN DE ORO CORREGIDA (SIN ERRORS DE ATRIBUTO)
    def obtener_o_generar_id_seg(df_seg, id_derecho_seleccionado):
        if df_seg is None or df_seg.empty:
            return "SEG-001"
            
        # Limpieza de seguridad en el DataFrame
        df_seg_limpio = df_seg.copy()
        df_seg_limpio["ID_Derecho"] = df_seg_limpio["ID_Derecho"].astype(str).str.strip()
        
        # Corrección aquí: Convertimos a string y aplicamos .strip() directamente
        id_buscar = str(id_derecho_seleccionado).strip()
        
        # 1. BUSQUEDA RELACIONAL: Si ya existe en el historial, hereda el primer SEG-XXX
        coincidencias = df_seg_limpio[df_seg_limpio["ID_Derecho"] == id_buscar]
        if not coincidencias.empty:
            return coincidencias["ID_Seguimiento"].values[0]
            
        # 2. GENERACIÓN CORRELATIVA: Si es nuevo, calcula el siguiente número
        if "ID_Seguimiento" in df_seg_limpio.columns:
            numeros = df_seg_limpio["ID_Seguimiento"].astype(str).str.extract(r'SEG-(\d+)').dropna().astype(int)
            if not numeros.empty:
                siguiente_numero = numeros.max().values[0] + 1
            else:
                siguiente_numero = 1
        else:
            siguiente_numero = 1
            
        return f"SEG-{siguiente_numero:03d}"

    # --- PESTAÑA 1: PANEL DE CONTROL ---
    with t_ver:
        st.write("### 📋 Historial Completo de Trámites por Derecho Minero")
        if not df_seguimiento.empty:
            # Ordenamos por código de seguimiento para que veas juntos todos los trámites de la misma concesión
            df_mostrar = df_seguimiento.sort_values(by="ID_Seguimiento", ascending=True)
            st.dataframe(df_mostrar, use_container_width=True)
        else:
            st.info("No hay trámites con hitos notificados todavía.")
            
    # --- PESTAÑA 2: REGISTRAR OBLIGACIÓN DE RESPUESTA ---
    with t_reg_oblig:
        st.write("### ⚠️ Cargar Nueva Notificación / Subsanación de Bioterra")
        
        if not df_concesiones.empty:
            with st.form("form_seguimiento_obligatorio"):
                col_o1, col_o2 = st.columns(2)
                with col_o1:
                    derecho_t = st.selectbox("Seleccione la Concesión:", df_concesiones["Nombre_Derecho"].unique(), key="sel_der_o")
                    acto_oblig = st.selectbox("Acto Administrativo Notificado:", [
                        "OBSERVACIONES",
                        "PUBLICACION DE CARTELES",
                        "REMATE POR SIMULTANEIDAD"
                    ])
                    
                    if acto_oblig == "REMATE POR SIMULTANEIDAD":
                        respuesta_vinculada = "Resolución del Remate"
                        dias_sug = 10
                    elif acto_oblig == "OBSERVACIONES":
                        respuesta_vinculada = "Levantamiento de Observaciones"
                        dias_sug = 15
                    else:
                        respuesta_vinculada = "Presentar Carteles"
                        dias_sug = 30
                        
                    st.info(f"🔄 **Acción Enlazada:** `{respuesta_vinculada}`")
                    copia_doc = st.text_input("Ruta de la copia digitalizada (PDF):", key="pdf_o")
                
                with col_o2:
                    f_notificacion = st.date_input("Fecha de Notificación:", key="f_not_o")
                    f_maxima = st.date_input("Fecha Máxima Legal (Límite):", value=pd.to_datetime(f_notificacion) + timedelta(days=dias_sug), key="f_max_o")
                    
                    subsanado = st.checkbox("¿Bioterra ya ingresó/envió la respuesta? (Pasará a SUBSANADO)", key="sub_o")
                    f_envio = st.date_input("Fecha de Envío / Atención:", key="f_env_o") if subsanado else None
                
                btn_seg_o = st.form_submit_button("Guardar Trámite en el Historial")
                
                if btn_seg_o:
                    id_der_sel = df_concesiones[df_concesiones["Nombre_Derecho"] == derecho_t]["ID_Derecho"].values[0]
                    f_envio_str = f_envio.strftime("%Y-%m-%d") if subsanado else "Pendiente de Envío"
                    estado_final_hito = f"✅ SUBSANADO ({respuesta_vinculada})" if subsanado else f"⚠️ PENDIENTE ({acto_oblig})"
                    
                    # Forzamos la asignación del ID de Seguimiento correcto antes de guardar
                    id_seg_final = obtener_o_generar_id_seg(df_seguimiento, id_der_sel)
                    
                    nueva_fila_seg = {
                        "ID_Seguimiento": id_seg_final,  # <--- AQUÍ: Siempre mantiene el primero asignado
                        "ID_Derecho": id_der_sel,
                        "Ruta_Legal": "Obligación de Respuesta",
                        "Hito_Actual": estado_final_hito,
                        "Fecha_Notificacion": f_notificacion.strftime("%Y-%m-%d"),
                        "Fecha_Limite_Maxima": f_maxima.strftime("%Y-%m-%d"),
                        "Fecha_Envio_Subsanacion": f_envio_str,
                        "Copia_Petitorio_Ruta": copia_doc,
                        "Estado_Hito": "Completado" if subsanado else "Vigente / En Alerta"
                    }
                    
                    df_seguimiento = pd.concat([df_seguimiento, pd.DataFrame([nueva_fila_seg])], ignore_index=True)
                    st.success(f"🎉 Trámite registrado con éxito. Se asignó el código ligado: `{id_seg_final}`")
                    
                    # Sincronizar maestro general
                    df_concesiones.loc[df_concesiones["ID_Derecho"] == id_der_sel, "Estado_Fase"] = estado_final_hito
                    guardar_datos(df_concesiones, "Petitorios_Concesiones")
                    guardar_datos(df_seguimiento, "Seguimiento_Tramites")
                    st.rerun()
        else:
            st.info("No hay concesiones mapeadas.")

    # --- PESTAÑA 3: REGISTRAR CICLO FINAL ---
    with t_reg_info:
        st.write("### ℹ️ Registrar Evolución o Hito Final de la Autoridad")
        
        if not df_concesiones.empty:
            with st.form("form_seguimiento_informativo"):
                col_i1, col_i2 = st.columns(2)
                with col_i1:
                    derecho_t_i = st.selectbox("Seleccione la Concesión:", df_concesiones["Nombre_Derecho"].unique(), key="sel_der_i")
                    acto_info = st.selectbox("Nuevo Hito a Consignar:", [
                        "RESOLUCION DE PRESIDENCIA (Titulación)", 
                        "CONSENTIMIENTO", 
                        "INSCRIPCION EN SUNARP"
                    ])
                    copia_doc_i = st.text_input("Ruta de la copia digitalizada (PDF/Ficha):", key="pdf_i")
                
                with col_i2:
                    f_emision = st.date_input("Fecha de Emisión / Inscripción Real:", key="f_not_i")
                
                btn_seg_i = st.form_submit_button("Añadir Hito Final al Historial")
                
                if btn_seg_i:
                    id_der_sel = df_concesiones[df_concesiones["Nombre_Derecho"] == derecho_t_i]["ID_Derecho"].values[0]
                    
                    if "PRESIDENCIA" in acto_info:
                        hito_para_guardar = "📜 RESOLUCIÓN DE PRESIDENCIA"
                    elif "CONSENTIMIENTO" in acto_info:
                        hito_para_guardar = "🤝 CONSENTIMIENTO"
                    else:
                        hito_para_guardar = "🏛️ INSCRIPCIÓN EN SUNARP"
                    
                    # Forzamos la asignación del ID de Seguimiento correcto antes de guardar
                    id_seg_final = obtener_o_generar_id_seg(df_seguimiento, id_der_sel)
                    
                    nueva_fila_info = {
                        "ID_Seguimiento": id_seg_final,  # <--- AQUÍ: Reutiliza el código sin importar cuántas filas existan
                        "ID_Derecho": id_der_sel,
                        "Ruta_Legal": "Ciclo Final Autoridad",
                        "Hito_Actual": hito_para_guardar,
                        "Fecha_Notificacion": f_emision.strftime("%Y-%m-%d"),
                        "Fecha_Limite_Maxima": "N/A",
                        "Fecha_Envio_Subsanacion": "N/A",
                        "Copia_Petitorio_Ruta": copia_doc_i,
                        "Estado_Hito": "Archivado / Concluido"
                    }
                    
                    df_seguimiento = pd.concat([df_seguimiento, pd.DataFrame([nueva_fila_info])], ignore_index=True)
                    st.success(f"🎉 Hito final añadido al historial. Código de seguimiento respetado: `{id_seg_final}`")
                    
                    # Sincronizar maestro general
                    df_concesiones.loc[df_concesiones["ID_Derecho"] == id_der_sel, "Estado_Fase"] = hito_para_guardar
                    guardar_datos(df_concesiones, "Petitorios_Concesiones")
                    guardar_datos(df_seguimiento, "Seguimiento_Tramites")
                    st.rerun()
        else:
            st.info("No hay concesiones mapeadas.")

# ==========================================
# MÓDULO 5: CONTROL DE PAGOS
# ==========================================
# ==========================================
# 💰 MÓDULO 5: CONTROL DE PAGOS / VIGENCIA (CON N° DE OPERACIÓN Y FECHA)
# ==========================================
elif menu == "💰 Control de Pagos / Vigencia":
    st.subheader("Control Financiero de Derechos de Vigencia y Penalidades")
    
    tab_p1, tab_p2 = st.tabs(["📊 Historial de Obligaciones Financieras", "💸 Registrar / Modificar Pago Bancario"])
   
    # --- PESTAÑA 1: HISTORIAL ---
    with tab_p1:
        st.write("### 🗃️ Registro de Obligaciones y Comprobantes")
        if not df_vigencias.empty:
            # Mostramos el dataframe con las nuevas columnas incluidas si existen
            st.dataframe(df_vigencias, use_container_width=True)
        else:
            st.info("No se registran obligaciones financieras o pagos archivados en el sistema.")
            
    # --- PESTAÑA 2: REGISTRAR PAGO ---
    with tab_p2:
        st.write("### 💸 Indexar Depósito de Derecho de Vigencia")
        st.markdown("<small style='color:gray;'>Registre los datos del voucher de pago para asegurar el sustento ante el INGEMMET / DREM.</small>", unsafe_allow_html=True)
        
        if not df_concesiones.empty:
            with st.form("form_vigencias_avanzado"):
                col_p1, col_p2 = st.columns(2)
                
                with col_p1:
                    concesion_sel = st.selectbox("Seleccione la Concesión / Petitorio:", df_concesiones["Nombre_Derecho"].unique())
                    anio = st.number_input("Año de la Obligación (Anualidad):", min_value=2020, max_value=2035, value=2026)
                    monto = st.number_input("Monto Cancelado (USD):", min_value=0.0, step=10.0, value=300.0)
                    estado_p = st.selectbox("Estado de la Obligación:", ["Vigente / Pagado", "Pendiente", "Exonerado"])
                
                with col_p2:
                    # NUEVOS CAMPOS SOLICITADOS
                    f_pago_banco = st.date_input("Fecha de Pago en el Banco:")
                    nro_operacion = st.text_input("Número de Operación / Voucher:", placeholder="Ej: 00451278")
                    
                    st.caption("💡 Tip: Para PPM el derecho de vigencia estándar es de $1.00 por hectárea, PMA $0.50 y Régimen General $3.00.")
                
                btn_v = st.form_submit_button("Grabar Transacción Financiera")
                
                if btn_v:
                    id_der_sel = df_concesiones[df_concesiones["Nombre_Derecho"] == concesion_sel]["ID_Derecho"].values[0]
                    
                    # Estructuramos la nueva fila asegurando que se guarden los nuevos datos
                    nueva_fila_pago = {
                        "ID_Pago": f"PAG-{len(df_vigencias)+1:03d}",
                        "ID_Derecho": id_der_sel,
                        "Anio_Vigencia": int(anio),
                        "Monto_USD": float(monto),
                        "Estado_Pago": estado_p,
                        "Fecha_Pago": f_pago_banco.strftime("%Y-%m-%d") if estado_p == "Vigente / Pagado" else "N/A",
                        "Nro_Operacion": str(nro_operacion).strip() if (nro_operacion and estado_p == "Vigente / Pagado") else "N/A"
                    }
                    
                    # Inserción en el DataFrame de memoria
                    df_vigencias = pd.concat([df_vigencias, pd.DataFrame([nueva_fila_pago])], ignore_index=True)
                    
                    # Guardar permanentemente en la pestaña 'Control_Vigencias' del Excel
                    guardar_datos(df_vigencias, "Control_Vigencias")
                    
                    st.success(f"🎉 ¡Pago del año {anio} registrado con éxito! Operación N° `{nro_operacion}` archivada.")
                    st.rerun()
        else:
            st.info("Debe registrar al menos un petitorio minero para poder asociarle un pago.")

# ==========================================
# 👤 MÓDULO: ANÁLISIS Y RESUMEN POR ADMINISTRADOS (INTEGRADO Y ADAPTADO)
# ==========================================
elif menu == "👤 Análisis por Administrados":
    st.subheader("Tablero de Control y Calificación de Expedientes por Administrado")
    
    if df_administrados.empty:
        st.info("No hay datos de administrados registrados para realizar el análisis.")
    else:
        # 1. Asegurar limpieza y orden de los administrados utilizando las variables oficiales
        df_adm_limpio = df_administrados.copy()
        df_adm_limpio["Razon_Social"] = df_adm_limpio["Razon_Social"].astype(str).str.strip()
        lista_administrados = sorted(df_adm_limpio["Razon_Social"].unique())
        
        # 2. Copias de seguridad para cruce de información financiera y de concesiones
        df_concesiones_check = df_concesiones.copy() if not df_concesiones.empty else pd.DataFrame(columns=["ID_Administrado", "ID_Derecho", "Nombre_Derecho", "Hectareas"])
        df_pagos_check = df_vigencias.copy() if not df_vigencias.empty else pd.DataFrame(columns=["ID_Derecho", "Monto_USD", "Estado_Pago"])
        df_calif_check = df_calificaciones.copy() if not df_calificaciones.empty else pd.DataFrame(columns=["ID_Administrado", "Estrato"])
        
        tab_general, tab_individual = st.tabs(["📊 Análisis General de Todos los Administrados", "🔍 Ver Resumen de un Administrado Seleccionado"])
        
        # ------------------------------------------------------------
        # SECCIÓN 1: ANÁLISIS GENERAL (TOTALES, OBLIGACIONES Y CALIFICACIÓN)
        # ------------------------------------------------------------
        with tab_general:
            st.write("### 🏢 Consolidado General de Clientes / Administrados")
            
            resumen_global = []
            for r_social in lista_administrados:
                # Obtener el ID_Administrado correspondiente a la Razón Social
                id_adm = df_adm_limpio[df_adm_limpio["Razon_Social"] == r_social]["ID_Administrado"].values[0]
                
                # Filtrar concesiones del administrado
                concesiones_adm = df_concesiones_check[df_concesiones_check["ID_Administrado"] == id_adm]
                total_concesiones = len(concesiones_adm)
                listado_nombres = ", ".join(concesiones_adm["Nombre_Derecho"].tolist()) if total_concesiones > 0 else "Sin concesiones cargadas"
                
                # Calcular obligaciones de pago pendientes cruzando por ID_Derecho
                ids_derechos = concesiones_adm["ID_Derecho"].tolist()
                pagos_adm = df_pagos_check[df_pagos_check["ID_Derecho"].isin(ids_derechos)]
                pendientes_pago = pagos_adm[pagos_adm["Estado_Pago"] == 'Pendiente'] if not pagos_adm.empty else pd.DataFrame()
                monto_pendiente = pendientes_pago["Monto_USD"].sum() if not pendientes_pago.empty else 0.0
                
                # Verificar Calificación (Estrato del Módulo 2)
                calif_adm = df_calif_check[df_calif_check["ID_Administrado"] == id_adm]
                if not calif_adm.empty and "Estrato" in calif_adm.columns:
                    calif_str = calif_adm["Estrato"].values[0]
                else:
                    calif_str = "Sin Calificación Registrada"
                    
                resumen_global.append({
                    "Razón Social / Administrado": r_social,
                    "Total Concesiones": total_concesiones,
                    "Lista de Concesiones": listado_nombres,
                    "Deuda Pendiente (USD)": f"$ {monto_pendiente:,.2f}",
                    "Estrato / Calificación": calif_str
                })
            
            df_resumen_total = pd.DataFrame(resumen_global)
            st.dataframe(df_resumen_total, use_container_width=True, hide_index=True)
            
            # Métricas rápidas globales
            st.write("---")
            col_m1, col_m2 = st.columns(2)
            col_m1.metric("Total Administrados Únicos", len(lista_administrados))
            col_m2.metric("Total Concesiones en Cartera", len(df_concesiones_check))

        # ------------------------------------------------------------
        # SECCIÓN 2: RESUMEN POR ADMINISTRADO SELECCIONADO
        # ------------------------------------------------------------
        with tab_individual:
            st.write("### 👤 Ficha Informativa por Administrado")
            adm_seleccionado = st.selectbox("Seleccione el Administrado a Inspeccionar:", lista_administrados, key="sb_analisis_individual")
            
            if adm_seleccionado:
                # Obtener ID del Administrado seleccionado
                id_adm_sel = df_adm_limpio[df_adm_limpio["Razon_Social"] == adm_seleccionado]["ID_Administrado"].values[0]
                
                # Filtros específicos por ID_Administrado
                concesiones_sel = df_concesiones_check[df_concesiones_check["ID_Administrado"] == id_adm_sel]
                ids_sel = concesiones_sel["ID_Derecho"].tolist()
                
                st.markdown(f"## **Titular:** {adm_seleccionado}")
                
                # Grid de KPI's individuales
                c1, c2, c3 = st.columns(3)
                c1.metric("Concesiones Registradas", len(concesiones_sel))
                
                # Cruce financiero por ID_Derecho
                pagos_sel = df_pagos_check[df_pagos_check["ID_Derecho"].isin(ids_sel)]
                deuda_sel = pagos_sel[pagos_sel["Estado_Pago"] == 'Pendiente']["Monto_USD"].sum() if not pagos_sel.empty else 0.0
                c2.metric("Obligaciones Pendientes", f"$ {deuda_sel:,.2f}", delta="- Al día" if deuda_sel == 0 else "⚠️ Revisar pagos", delta_color="inverse")
                
                # Obtención de la Calificación/Estrato desde el DataFrame de Calificaciones
                calif_sel = df_calif_check[df_calif_check["ID_Administrado"] == id_adm_sel]
                estrato_individual = calif_sel["Estrato"].values[0] if not calif_sel.empty else "No Asignado"
                c3.metric("Estrato Técnico", estrato_individual)
                
                # Desglose detallado de Propiedades Mineras
                st.write("#### 📂 Desglose de Propiedades Mineras")
                if not concesiones_sel.empty:
                    # Dinámicamente mostramos las columnas disponibles en tu df_concesiones original
                    columnas_visibles = ["ID_Derecho", "Nombre_Derecho", "Hectareas", "Estado", "Estado_Pago", "Fase"]
                    columnas_existentes = [c for c in columnas_visibles if c in concesiones_sel.columns]
                    
                    if con_id_y_nombre := [c for c in ["ID_Derecho", "Nombre_Derecho"] if c in concesiones_sel.columns]:
                        # Si faltan columnas de visualización por defecto, nos aseguramos de mostrar al menos los datos clave
                        st.dataframe(concesiones_sel[list(set(con_id_y_nombre + columnas_existentes))], use_container_width=True, hide_index=True)
                    else:
                        st.dataframe(concesiones_sel, use_container_width=True, hide_index=True)
                else:
                    st.info("Este administrado no cuenta con derechos mineros asociados en este momento.")
                
                # Historial Financiero del Administrado
                st.write("#### 💳 Estado de Cuentas (Derechos de Vigencia / Penalidades)")
                if not pagos_sel.empty:
                    st.dataframe(pagos_sel, use_container_width=True, hide_index=True)
                else:
                    st.info("Este administrado no registra transacciones financieras en la base de datos.")
                    # ==========================================
# ==========================================
# 🔧 MÓDULO: ACTUALIZACIÓN Y CORRECCIÓN DE DATOS (CON VIGENCIAS)
# ==========================================
elif menu == "🔧 Actualización de Datos":
    st.subheader("Centro de Modificación y Corrección del Catastro")
    st.markdown("Use este módulo para corregir errores de digitación o reflejar actualizaciones legales de titulares, derechos o estados de pago.")

    ARCHIVO_OBJETIVO = "PETITORIOS MINEROS.xlsx"

    # Añadimos la tercera opción para Vigencias
    tipo_edicion = st.radio(
        "Seleccione el tipo de registro a modificar:",
        ["👤 Datos del Administrado / Titular", "📐 Datos de la Concesión Minera", "💳 Datos de Vigencias / Pagos"],
        horizontal=True
    )

    # ------------------------------------------------------------
    # OPCIÓN A: MODIFICAR ADMINISTRADOS
    # ------------------------------------------------------------
    if tipo_edicion == "👤 Datos del Administrado / Titular":
        if df_administrados.empty:
            st.info("No hay datos de administrados registrados para modificar.")
        else:
            st.write("### Editar Información de Administrado")
            
            df_adm_mod = df_administrados.copy()
            df_adm_mod["Razon_Social"] = df_adm_mod["Razon_Social"].astype(str).str.strip()
            lista_administrados = sorted(df_adm_mod["Razon_Social"].unique())
            
            adm_a_editar = st.selectbox("Seleccione el Administrado a modificar:", lista_administrados, key="sb_edit_adm")
            
            idx_adm = df_administrados[df_administrados["Razon_Social"].astype(str).str.strip() == adm_a_editar].index[0]
            datos_actuales_adm = df_administrados.loc[idx_adm]

            with st.form("form_editar_administrado"):
                st.info(f"Modificando ID_Administrado: `{datos_actuales_adm['ID_Administrado']}`")
                
                nueva_razon_social = st.text_input("Razón Social / Nombre Completo:", value=str(datos_actuales_adm["Razon_Social"]))
                ruc_actual = str(datos_actuales_adm["RUC"]) if "RUC" in df_administrados.columns else ""
                nuevo_ruc = st.text_input("Número de RUC (Opcional):", value=ruc_actual)

                btn_guardar_adm = st.form_submit_button("💾 Guardar Cambios en Administrado")

                if btn_guardar_adm:
                    if not nueva_razon_social.strip():
                        st.error("🚨 La Razón Social no puede quedar vacía.")
                    else:
                        if "df_administrados" in st.session_state:
                            st.session_state.df_administrados.at[idx_adm, "Razon_Social"] = nueva_razon_social.strip()
                            if "RUC" in st.session_state.df_administrados.columns:
                                st.session_state.df_administrados.at[idx_adm, "RUC"] = nuevo_ruc.strip()
                        else:
                            df_administrados.at[idx_adm, "Razon_Social"] = nueva_razon_social.strip()
                            if "RUC" in df_administrados.columns:
                                df_administrados.at[idx_adm, "RUC"] = nuevo_ruc.strip()
                        
                        try:
                            df_a_guardar = st.session_state.df_administrados if "df_administrados" in st.session_state else df_administrados
                            with pd.ExcelWriter(ARCHIVO_OBJETIVO, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                                df_a_guardar.to_excel(writer, sheet_name='Administrados', index=False)
                            st.success(f"✅ ¡Cambios aplicados permanentemente!")
                            st.balloons()
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error al escribir en Excel: {e}")

    # ------------------------------------------------------------
    # OPCIÓN B: MODIFICAR CONCESIONES
    # ------------------------------------------------------------
    elif tipo_edicion == "📐 Datos de la Concesión Minera":
        if df_concesiones.empty:
            st.info("No hay datos de concesiones registrados para modificar.")
        else:
            st.write("### Editar Propiedades de la Concesión")
            
            df_con_mod = df_concesiones.copy()
            df_con_mod["Selector_Nombre"] = df_con_mod["ID_Derecho"].astype(str).str.strip() + " - " + df_con_mod["Nombre_Derecho"].astype(str).str.strip()
            lista_concesiones = sorted(df_con_mod["Selector_Nombre"].unique())
            
            concesion_a_editar = st.selectbox("Seleccione el Derecho Minero a modificar:", lista_concesiones, key="sb_edit_con")
            
            idx_con = df_con_mod[df_con_mod["Selector_Nombre"] == concesion_a_editar].index[0]
            datos_actuales_con = df_concesiones.loc[idx_con]

            df_adm_aux = df_administrados.copy()
            df_adm_aux["Razon_Social"] = df_adm_aux["Razon_Social"].astype(str).str.strip()
            lista_id_adm = list(df_adm_aux["ID_Administrado"].unique())
            lista_razon_adm = list(df_adm_aux["Razon_Social"].unique())

            with st.form("form_editar_concesion"):
                col_e1, col_e2 = st.columns(2)
                
                with col_e1:
                    nuevo_nombre_derecho = st.text_input("Nombre del Derecho Minero:", value=str(datos_actuales_con["Nombre_Derecho"]))
                    val_ha = float(datos_actuales_con["Hectareas"]) if "Hectareas" in datos_actuales_con and pd.notna(datos_actuales_con["Hectareas"]) else 0.0
                    nuevas_hectareas = st.number_input("Extensión (Hectáreas):", value=val_ha, min_value=0.0, step=1.0)

                with col_e2:
                    st.markdown("**Asignación / Transferencia de Titularidad**")
                    id_actual_dueno = datos_actuales_con["ID_Administrado"]
                    try:
                        idx_defecto_dueno = lista_id_adm.index(id_actual_dueno)
                    except ValueError:
                        idx_defecto_dueno = 0

                    nuevo_dueno_razon = st.selectbox("Administrado Responsable (Titular):", options=lista_razon_adm, index=idx_defecto_dueno)
                    nuevo_id_administrado = df_adm_aux[df_adm_aux["Razon_Social"] == nuevo_dueno_razon]["ID_Administrado"].values[0]

                st.write("---")
                btn_guardar_con = st.form_submit_button("💾 Guardar Cambios en Concesión")

                if btn_guardar_con:
                    if not nuevo_nombre_derecho.strip():
                        st.error("🚨 El nombre del derecho minero no puede estar vacío.")
                    else:
                        if "df_concesiones" in st.session_state:
                            st.session_state.df_concesiones.at[idx_con, "Nombre_Derecho"] = nuevo_nombre_derecho.strip().upper()
                            st.session_state.df_concesiones.at[idx_con, "Hectareas"] = nuevas_hectareas
                            st.session_state.df_concesiones.at[idx_con, "ID_Administrado"] = nuevo_id_administrado
                        else:
                            df_concesiones.at[idx_con, "Nombre_Derecho"] = nuevo_nombre_derecho.strip().upper()
                            df_concesiones.at[idx_con, "Hectareas"] = nuevas_hectareas
                            df_concesiones.at[idx_con, "ID_Administrado"] = nuevo_id_administrado
                        
                        try:
                            df_c_guardar = st.session_state.df_concesiones if "df_concesiones" in st.session_state else df_concesiones
                            with pd.ExcelWriter(ARCHIVO_OBJETIVO, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                                df_c_guardar.to_excel(writer, sheet_name='Concesiones', index=False)
                            st.success(f"✅ ¡Concesión modificada con éxito!")
                            st.balloons()
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error al escribir en Excel: {e}")

    # ------------------------------------------------------------
    # OPCIÓN C: MODIFICAR VIGENCIAS / OBLIGACIONES FINANCIERAS (NUEVO)
    # ------------------------------------------------------------
    elif tipo_edicion == "💳 Datos de Vigencias / Pagos":
        if df_vigencias.empty:
            st.info("No hay registros de obligaciones financieras / vigencias para modificar.")
        else:
            st.write("### Control de Obligaciones Financieras y Pagos")
            
            # Cruzamos temporalmente con concesiones para armar un selector entendible (ID - Nombre)
            df_vig_mod = df_vigencias.copy()
            if not df_concesiones.empty:
                df_vig_mod = df_vig_mod.merge(df_concesiones[["ID_Derecho", "Nombre_Derecho"]], on="ID_Derecho", how="left")
                df_vig_mod["Selector_Vigencia"] = df_vig_mod["ID_Derecho"].astype(str) + " - " + df_vig_mod["Nombre_Derecho"].fillna("Sin Nombre").astype(str)
            else:
                df_vig_mod["Selector_Vigencia"] = df_vig_mod["ID_Derecho"].astype(str)
                
            lista_obligaciones = sorted(df_vig_mod["Selector_Vigencia"].unique())
            vigencia_a_editar = st.selectbox("Seleccione la Obligación del Derecho a modificar:", lista_obligaciones, key="sb_edit_vig")
            
            # Ubicar el índice real en la estructura base
            id_derecho_sel = df_vig_mod[df_vig_mod["Selector_Vigencia"] == vigencia_a_editar]["ID_Derecho"].values[0]
            idx_vig = df_vigrencias[df_vigencias["ID_Derecho"] == id_derecho_sel].index[0] if 'df_vigrencias' in locals() else df_vigencias[df_vigencias["ID_Derecho"] == id_derecho_sel].index[0]
            datos_actuales_vig = df_vigencias.loc[idx_vig]

            with st.form("form_editar_vigencia"):
                st.markdown(f"Modificando Obligaciones del Derecho ID: `{id_derecho_sel}`")
                col_v1, col_v2 = st.columns(2)
                
                with col_v1:
                    val_monto = float(datos_actuales_vig["Monto_USD"]) if "Monto_USD" in datos_actuales_vig and pd.notna(datos_actuales_vig["Monto_USD"]) else 0.0
                    nuevo_monto = st.number_input("Monto de la Obligación (USD):", value=val_monto, min_value=0.0, step=10.0)
                
                with col_v2:
                    estado_actual = str(datos_actuales_vig["Estado_Pago"]).strip()
                    opciones_pago = ["Pendiente", "Pagado", "Exonerado"]
                    
                    try:
                        idx_defecto_pago = opciones_pago.index(estado_actual)
                    except ValueError:
                        idx_defecto_pago = 0
                        
                    nuevo_estado = st.selectbox("Estado del Pago / Obligación:", options=opciones_pago, index=idx_defecto_pago)

                st.write("---")
                btn_guardar_vig = st.form_submit_button("💾 Actualizar Estado de Cuenta / Vigencia")

                if btn_guardar_vig:
                    # 1. Modificar en Session State o memoria local
                    if "df_vigencias" in st.session_state:
                        st.session_state.df_vigencias.at[idx_vig, "Monto_USD"] = nuevo_monto
                        st.session_state.df_vigencias.at[idx_vig, "Estado_Pago"] = nuevo_estado
                    else:
                        df_vigencias.at[idx_vig, "Monto_USD"] = nuevo_monto
                        df_vigencias.at[idx_vig, "Estado_Pago"] = nuevo_estado
                    
                    # 2. Persistir permanentemente en el archivo Excel (Pestaña 'Vigencias')
                    try:
                        df_v_guardar = st.session_state.df_vigencias if "df_vigencias" in st.session_state else df_vigencias
                        with pd.ExcelWriter(ARCHIVO_OBJETIVO, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                            df_v_guardar.to_excel(writer, sheet_name='Vigencias', index=False) # Cambia 'Vigencias' si tu pestaña de pagos se llama diferente
                        st.success("✅ ¡Estado financiero de vigencia actualizado con éxito!")
                        st.balloons()
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error al escribir en Excel: {e}. Cierra el archivo si lo tienes abierto.")

# ---- PIE DE PÁGINA CORPORATIVO ----
st.markdown('<div class="footer">BIOTERRA — Consultoría y Gestión Ambiental Minera S.A.C.</div>', unsafe_allow_html=True)
# ---- PIE DE PÁGINA CORPORATIVO ----
st.markdown('<div class="footer">BIOTERRA — Consultoría y Gestión Ambiental Minera S.A.C.</div>', unsafe_allow_html=True)
# ---- PIE DE PÁGINA CORPORATIVO ----
st.markdown('<div class="footer">BIOTERRA — Consultoría y Gestión Ambiental Minera S.A.C.</div>', unsafe_allow_html=True)

# ---- PIE DE PÁGINA CORPORATIVO ----
st.markdown('<div class="footer">BIOTERRA — Consultoría y Gestión Ambiental Minera S.A.C.</div>', unsafe_allow_html=True)
