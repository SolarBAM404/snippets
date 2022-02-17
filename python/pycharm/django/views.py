class $name$ListView(ListView):
    paginate_by = $pageinator$
    model = $model$
    template_name = "$template_list$"
    
class $name$DetailView(DetailView):
    model = $model$
    template_name = "$template_detail$"
