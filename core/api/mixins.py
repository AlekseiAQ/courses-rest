class SerializedClassesMixin(object):
    serializer_classes = {}

    def get_serializer_class(self):
        try:
            return self.serializer_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
