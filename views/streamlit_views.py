from sfn_blueprint.views.base_view import StreamlitView

class StreamlitView(StreamlitView):
    def select_box(self, label: str, options: List[str],placeholder: Optional[str] = None, key: Optional[str] = None) -> str:
        return st.selectbox(label, options, placeholder=placeholder, key=key)

    