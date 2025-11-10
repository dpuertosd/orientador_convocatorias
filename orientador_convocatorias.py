import streamlit as st

st.set_page_config(page_title="Orientador de Convocatorias", page_icon="💡")

st.title("💬 Orientador de Convocatorias para Emprendedores")
st.write("Responde las siguientes preguntas para identificar la convocatoria más adecuada para tu proyecto.")

# --- Formulario interactivo ---
sector = st.selectbox("1️⃣ ¿En qué sector se desarrolla tu proyecto?", 
                      ["Selecciona...", "Agro", "Tecnología", "Turismo", "Manufactura", "Servicios", "Otro"])

formalizacion = st.selectbox("2️⃣ ¿Tu empresa o grupo está formalizado legalmente?", 
                             ["Selecciona...", "SAS", "Asociación", "Persona natural", "Otro"])

ubicacion = st.text_input("3️⃣ ¿En qué departamento o municipio opera principalmente tu emprendimiento?")

equipo = st.number_input("4️⃣ ¿Cuántas personas hacen parte del equipo o asociación?", min_value=1, step=1)

etapa = st.selectbox("5️⃣ ¿En qué etapa está tu proyecto?", 
                     ["Idea", "En marcha", "Consolidado", "Expansión"])

monto = st.number_input("6️⃣ ¿Cuál es el monto aproximado de apoyo que estás buscando?", min_value=0, step=1000)

enfoque = st.selectbox("7️⃣ ¿Tu proyecto tiene enfoque ambiental, social o comunitario?", 
                       ["Ninguno", "Ambiental", "Social", "Comunitario"])

capital = st.radio("8️⃣ ¿Cuentas con capital propio para aportar al proyecto?", ["Sí", "No"])

# --- Análisis y resultado ---
if st.button("Analizar"):
    st.subheader("🔎 Resultados del análisis")

    # Lógica simple de compatibilidad
    if sector.lower() == "agro" and formalizacion.lower() in ["asociación", "otro"]:
        principal = "#131 – Economía Campesina"
        compat = "Alta"
        motivo = "Tu proyecto es rural/agropecuario y asociativo."
    elif enfoque in ["Ambiental", "Social", "Comunitario"]:
        principal = "#137 – Emprendimiento Verde"
        compat = "Alta"
        motivo = "Tiene impacto ambiental o comunitario."
    elif formalizacion == "SAS" and etapa in ["Consolidado", "Expansión"]:
        principal = "#122 – Fortalecimiento Empresarial"
        compat = "Media"
        motivo = "Tu empresa está formalizada y en crecimiento."
    else:
        principal = "Ninguna con compatibilidad fuerte"
        compat = "Baja"
        motivo = "Revisa formalización o enfoque productivo."

    st.markdown(f"**Convocatoria sugerida:** {principal}")
    st.markdown(f"**Compatibilidad:** {compat}")
    st.markdown(f"**Motivo:** {motivo}")

    # Check list de documentos
    if principal != "Ninguna con compatibilidad fuerte":
        st.subheader("📋 Documentos recomendados")
        st.write("""
        - Certificado de existencia y representación legal  
        - Copia del NIT  
        - Listado de integrantes activos  
        - Descripción del proyecto (1–2 páginas)  
        - Presupuesto detallado y cronograma  
        """)

---

### ▶️ 3. Ejecutar tu aplicación
En la terminal (donde guardaste el archivo), ejecutas:

```bash
streamlit run orientador_convocatorias.py
