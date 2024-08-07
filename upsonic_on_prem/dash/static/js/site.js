
hljs.highlightAll();


!function(a, b) {
    "use strict";
    "function" == typeof define && define.amd ? define([], b) : "object" == typeof module && module.exports ? module.exports = b() : (a.AnchorJS = b(),
    a.anchors = new a.AnchorJS)
}(this, function() {
    "use strict";
    return function(c) {
        function a(a) {
            a.icon = Object.prototype.hasOwnProperty.call(a, "icon") ? a.icon : "",
            a.visible = Object.prototype.hasOwnProperty.call(a, "visible") ? a.visible : "hover",
            a.placement = Object.prototype.hasOwnProperty.call(a, "placement") ? a.placement : "right",
            a.ariaLabel = Object.prototype.hasOwnProperty.call(a, "ariaLabel") ? a.ariaLabel : "Anchor",
            a.class = Object.prototype.hasOwnProperty.call(a, "class") ? a.class : "",
            a.base = Object.prototype.hasOwnProperty.call(a, "base") ? a.base : "",
            a.truncate = Object.prototype.hasOwnProperty.call(a, "truncate") ? Math.floor(a.truncate) : 64,
            a.titleText = Object.prototype.hasOwnProperty.call(a, "titleText") ? a.titleText : ""
        }
        function b(a) {
            var b;
            if ("string" == typeof a || a instanceof String)
                b = [].slice.call(document.querySelectorAll(a));
            else {
                if (!(Array.isArray(a) || a instanceof NodeList))
                    throw new TypeError("The selector provided to AnchorJS was invalid.");
                b = [].slice.call(a)
            }
            return b
        }
        this.options = c || {},
        this.elements = [],
        a(this.options),
        this.isTouchDevice = function() {
            return Boolean("ontouchstart"in window || window.TouchEvent || window.DocumentTouch && document instanceof DocumentTouch)
        }
        ,
        this.add = function(k) {
            var e, o, h, c, i, n, p, g, d, m, j, f, l = [];
            if (a(this.options),
            "touch" === (m = this.options.visible) && (m = this.isTouchDevice() ? "always" : "hover"),
            0 === (e = b(k = k || "h2, h3, h4, h5, h6")).length)
                return this;
            for (null === document.head.querySelector("style.anchorjs") && ((f = document.createElement("style")).className = "anchorjs",
            f.appendChild(document.createTextNode("")),
            void 0 === (k = document.head.querySelector('[rel="stylesheet"],style')) ? document.head.appendChild(f) : document.head.insertBefore(f, k),
            f.sheet.insertRule(".anchorjs-link{opacity:0;text-decoration:none;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}", f.sheet.cssRules.length),
            f.sheet.insertRule(":hover>.anchorjs-link,.anchorjs-link:focus{opacity:1}", f.sheet.cssRules.length),
            f.sheet.insertRule("[data-anchorjs-icon]::after{content:attr(data-anchorjs-icon)}", f.sheet.cssRules.length),
            f.sheet.insertRule('@font-face{font-family:anchorjs-icons;src:url(data:n/a;base64,AAEAAAALAIAAAwAwT1MvMg8yG2cAAAE4AAAAYGNtYXDp3gC3AAABpAAAAExnYXNwAAAAEAAAA9wAAAAIZ2x5ZlQCcfwAAAH4AAABCGhlYWQHFvHyAAAAvAAAADZoaGVhBnACFwAAAPQAAAAkaG10eASAADEAAAGYAAAADGxvY2EACACEAAAB8AAAAAhtYXhwAAYAVwAAARgAAAAgbmFtZQGOH9cAAAMAAAAAunBvc3QAAwAAAAADvAAAACAAAQAAAAEAAHzE2p9fDzz1AAkEAAAAAADRecUWAAAAANQA6R8AAAAAAoACwAAAAAgAAgAAAAAAAAABAAADwP/AAAACgAAA/9MCrQABAAAAAAAAAAAAAAAAAAAAAwABAAAAAwBVAAIAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAMCQAGQAAUAAAKZAswAAACPApkCzAAAAesAMwEJAAAAAAAAAAAAAAAAAAAAARAAAAAAAAAAAAAAAAAAAAAAQAAg//0DwP/AAEADwABAAAAAAQAAAAAAAAAAAAAAIAAAAAAAAAIAAAACgAAxAAAAAwAAAAMAAAAcAAEAAwAAABwAAwABAAAAHAAEADAAAAAIAAgAAgAAACDpy//9//8AAAAg6cv//f///+EWNwADAAEAAAAAAAAAAAAAAAAACACEAAEAAAAAAAAAAAAAAAAxAAACAAQARAKAAsAAKwBUAAABIiYnJjQ3NzY2MzIWFxYUBwcGIicmNDc3NjQnJiYjIgYHBwYUFxYUBwYGIwciJicmNDc3NjIXFhQHBwYUFxYWMzI2Nzc2NCcmNDc2MhcWFAcHBgYjARQGDAUtLXoWOR8fORYtLTgKGwoKCjgaGg0gEhIgDXoaGgkJBQwHdR85Fi0tOAobCgoKOBoaDSASEiANehoaCQkKGwotLXoWOR8BMwUFLYEuehYXFxYugC44CQkKGwo4GkoaDQ0NDXoaShoKGwoFBe8XFi6ALjgJCQobCjgaShoNDQ0NehpKGgobCgoKLYEuehYXAAAADACWAAEAAAAAAAEACAAAAAEAAAAAAAIAAwAIAAEAAAAAAAMACAAAAAEAAAAAAAQACAAAAAEAAAAAAAUAAQALAAEAAAAAAAYACAAAAAMAAQQJAAEAEAAMAAMAAQQJAAIABgAcAAMAAQQJAAMAEAAMAAMAAQQJAAQAEAAMAAMAAQQJAAUAAgAiAAMAAQQJAAYAEAAMYW5jaG9yanM0MDBAAGEAbgBjAGgAbwByAGoAcwA0ADAAMABAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAH//wAP) format("truetype")}', f.sheet.cssRules.length)),
            f = document.querySelectorAll("[id]"),
            o = [].map.call(f, function(a) {
                return a.id
            }),
            c = 0; c < e.length; c++)
                if (this.hasAnchorJSLink(e[c]))
                    l.push(c);
                else {
                    if (e[c].hasAttribute("id"))
                        h = e[c].getAttribute("id");
                    else if (e[c].hasAttribute("data-anchor-id"))
                        h = e[c].getAttribute("data-anchor-id");
                    else {
                        for (g = p = this.urlify(e[c].textContent),
                        n = 0; i = o.indexOf(g = void 0 !== i ? p + "-" + n : g),
                        n += 1,
                        -1 !== i; )
                            ;
                        i = void 0,
                        o.push(g),
                        e[c].setAttribute("id", g),
                        h = g
                    }
                    (d = document.createElement("a")).className = "anchorjs-link " + this.options.class,
                    d.setAttribute("aria-label", this.options.ariaLabel),
                    d.setAttribute("data-anchorjs-icon", this.options.icon),
                    this.options.titleText && (d.title = this.options.titleText),
                    j = document.querySelector("base") ? window.location.pathname + window.location.search : "",
                    j = this.options.base || j,
                    d.href = j + "#" + h,
                    "always" === m && (d.style.opacity = "1"),
                    "" === this.options.icon && (d.style.font = "1em/1 anchorjs-icons",
                    "left" === this.options.placement && (d.style.lineHeight = "inherit")),
                    "left" === this.options.placement ? (d.style.position = "absolute",
                    d.style.marginLeft = "-1em",
                    d.style.paddingRight = ".5em",
                    e[c].insertBefore(d, e[c].firstChild)) : (d.style.paddingLeft = ".375em",
                    e[c].appendChild(d))
                }
            for (c = 0; c < l.length; c++)
                e.splice(l[c] - c, 1);
            return this.elements = this.elements.concat(e),
            this
        }
        ,
        this.remove = function(f) {
            for (var d, e, c = b(f), a = 0; a < c.length; a++)
                (e = c[a].querySelector(".anchorjs-link")) && (-1 !== (d = this.elements.indexOf(c[a])) && this.elements.splice(d, 1),
                c[a].removeChild(e));
            return this
        }
        ,
        this.removeAll = function() {
            this.remove(this.elements)
        }
        ,
        this.urlify = function(b) {
            var c = document.createElement("textarea");
            return c.innerHTML = b,
            b = c.value,
            this.options.truncate || a(this.options),
            b.trim().replace(/'/gi, "").replace(/[& +$,:;=?@"#{}|^~[`%!'<>\]./()*\\\n\t\b\v\u00A0]/g, "-").replace(/-{2,}/g, "-").substring(0, this.options.truncate).replace(/^-+|-+$/gm, "").toLowerCase()
        }
        ,
        this.hasAnchorJSLink = function(a) {
            var b = a.firstChild && -1 < (" " + a.firstChild.className + " ").indexOf(" anchorjs-link ")
              , a = a.lastChild && -1 < (" " + a.lastChild.className + " ").indexOf(" anchorjs-link ");
            return b || a || !1
        }
    }
}),
!function(b, a) {
    "object" == typeof exports && "object" == typeof module ? module.exports = a() : "function" == typeof define && define.amd ? define([], a) : "object" == typeof exports ? exports.ClipboardJS = a() : b.ClipboardJS = a()
}(this, function() {
    return c = {
        134: function(p, a, b) {
            "use strict";
            var n, m, f, i, g;
            b.d(a, {
                default: function() {
                    return g
                }
            }),
            a = b(279),
            n = b.n(a),
            a = b(370),
            m = b.n(a),
            a = b(817),
            f = b.n(a);
            function j(a) {
                return (j = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(a) {
                    return typeof a
                }
                : function(a) {
                    return a && "function" == typeof Symbol && a.constructor === Symbol && a !== Symbol.prototype ? "symbol" : typeof a
                }
                )(a)
            }
            function h(d, c) {
                for (var b = 0, a; b < c.length; b++)
                    a = c[b],
                    a.enumerable = a.enumerable || !1,
                    a.configurable = !0,
                    "value"in a && (a.writable = !0),
                    Object.defineProperty(d, a.key, a)
            }
            i = function() {
                function a(b) {
                    !function(b) {
                        if (!(b instanceof a))
                            throw new TypeError("Cannot call a class as a function")
                    }(this),
                    this.resolveOptions(b),
                    this.initSelection()
                }
                var b, c, d;
                return b = a,
                (c = [{
                    key: "resolveOptions",
                    value: function() {
                        var a = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {};
                        this.action = a.action,
                        this.container = a.container,
                        this.emitter = a.emitter,
                        this.target = a.target,
                        this.text = a.text,
                        this.trigger = a.trigger,
                        this.selectedText = ""
                    }
                }, {
                    key: "initSelection",
                    value: function() {
                        this.text ? this.selectFake() : this.target && this.selectTarget()
                    }
                }, {
                    key: "createFakeElement",
                    value: function() {
                        var a = "rtl" === document.documentElement.getAttribute("dir");
                        return this.fakeElem = document.createElement("textarea"),
                        this.fakeElem.style.fontSize = "12pt",
                        this.fakeElem.style.border = "0",
                        this.fakeElem.style.padding = "0",
                        this.fakeElem.style.margin = "0",
                        this.fakeElem.style.position = "absolute",
                        this.fakeElem.style[a ? "right" : "left"] = "-9999px",
                        a = window.pageYOffset || document.documentElement.scrollTop,
                        this.fakeElem.style.top = "".concat(a, "px"),
                        this.fakeElem.setAttribute("readonly", ""),
                        this.fakeElem.value = this.text,
                        this.fakeElem
                    }
                }, {
                    key: "selectFake",
                    value: function() {
                        var b = this
                          , a = this.createFakeElement();
                        this.fakeHandlerCallback = function() {
                            return b.removeFake()
                        }
                        ,
                        this.fakeHandler = this.container.addEventListener("click", this.fakeHandlerCallback) || !0,
                        this.container.appendChild(a),
                        this.selectedText = f()(a),
                        this.copyText(),
                        this.removeFake()
                    }
                }, {
                    key: "removeFake",
                    value: function() {
                        this.fakeHandler && (this.container.removeEventListener("click", this.fakeHandlerCallback),
                        this.fakeHandler = null,
                        this.fakeHandlerCallback = null),
                        this.fakeElem && (this.container.removeChild(this.fakeElem),
                        this.fakeElem = null)
                    }
                }, {
                    key: "selectTarget",
                    value: function() {
                        this.selectedText = f()(this.target),
                        this.copyText()
                    }
                }, {
                    key: "copyText",
                    value: function() {
                        var a;
                        try {
                            a = document.execCommand(this.action)
                        } catch (b) {
                            a = !1
                        }
                        this.handleResult(a)
                    }
                }, {
                    key: "handleResult",
                    value: function(a) {
                        this.emitter.emit(a ? "success" : "error", {
                            action: this.action,
                            text: this.selectedText,
                            trigger: this.trigger,
                            clearSelection: this.clearSelection.bind(this)
                        })
                    }
                }, {
                    key: "clearSelection",
                    value: function() {
                        this.trigger && this.trigger.focus(),
                        document.activeElement.blur(),
                        window.getSelection().removeAllRanges()
                    }
                }, {
                    key: "destroy",
                    value: function() {
                        this.removeFake()
                    }
                }, {
                    key: "action",
                    set: function() {
                        var a = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : "copy";
                        if (this._action = a,
                        "copy" !== this._action && "cut" !== this._action)
                            throw new Error('Invalid "action" value, use either "copy" or "cut"')
                    },
                    get: function() {
                        return this._action
                    }
                }, {
                    key: "target",
                    set: function(a) {
                        if (void 0 !== a) {
                            if (!a || "object" !== j(a) || 1 !== a.nodeType)
                                throw new Error('Invalid "target" value, use a valid Element');
                            if ("copy" === this.action && a.hasAttribute("disabled"))
                                throw new Error('Invalid "target" attribute. Please use "readonly" instead of "disabled" attribute');
                            if ("cut" === this.action && (a.hasAttribute("readonly") || a.hasAttribute("disabled")))
                                throw new Error('Invalid "target" attribute. You can\'t cut text from elements with "readonly" or "disabled" attributes');
                            this._target = a
                        }
                    },
                    get: function() {
                        return this._target
                    }
                }]) && h(b.prototype, c),
                d && h(b, d),
                a
            }();
            function c(a) {
                return (c = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(a) {
                    return typeof a
                }
                : function(a) {
                    return a && "function" == typeof Symbol && a.constructor === Symbol && a !== Symbol.prototype ? "symbol" : typeof a
                }
                )(a)
            }
            function k(d, c) {
                for (var b = 0, a; b < c.length; b++)
                    a = c[b],
                    a.enumerable = a.enumerable || !1,
                    a.configurable = !0,
                    "value"in a && (a.writable = !0),
                    Object.defineProperty(d, a.key, a)
            }
            function l(a, b) {
                return (l = Object.setPrototypeOf || function(a, b) {
                    return a.__proto__ = b,
                    a
                }
                )(a, b)
            }
            function o(a) {
                var b = function() {
                    if ("undefined" == typeof Reflect || !Reflect.construct)
                        return !1;
                    if (Reflect.construct.sham)
                        return !1;
                    if ("function" == typeof Proxy)
                        return !0;
                    try {
                        return Date.prototype.toString.call(Reflect.construct(Date, [], function() {})),
                        !0
                    } catch (a) {
                        return !1
                    }
                }();
                return function() {
                    var e, f = d(a);
                    return e = b ? (e = d(this).constructor,
                    Reflect.construct(f, arguments, e)) : f.apply(this, arguments),
                    f = this,
                    !(e = e) || "object" !== c(e) && "function" != typeof e ? function(a) {
                        if (void 0 !== a)
                            return a;
                        throw new ReferenceError("this hasn't been initialised - super() hasn't been called")
                    }(f) : e
                }
            }
            function d(a) {
                return (d = Object.setPrototypeOf ? Object.getPrototypeOf : function(a) {
                    return a.__proto__ || Object.getPrototypeOf(a)
                }
                )(a)
            }
            function e(a, b) {
                if (a = "data-clipboard-".concat(a),
                b.hasAttribute(a))
                    return b.getAttribute(a)
            }
            g = function() {
                !function(b, a) {
                    if ("function" != typeof a && null !== a)
                        throw new TypeError("Super expression must either be null or a function");
                    b.prototype = Object.create(a && a.prototype, {
                        constructor: {
                            value: b,
                            writable: !0,
                            configurable: !0
                        }
                    }),
                    a && l(b, a)
                }(a, n());
                var b, f, d, g = o(a);
                function a(c, d) {
                    var b;
                    return function(b) {
                        if (!(b instanceof a))
                            throw new TypeError("Cannot call a class as a function")
                    }(this),
                    (b = g.call(this)).resolveOptions(d),
                    b.listenClick(c),
                    b
                }
                return b = a,
                d = [{
                    key: "isSupported",
                    value: function() {
                        var a = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : ["copy", "cut"]
                          , a = "string" == typeof a ? [a] : a
                          , b = !!document.queryCommandSupported;
                        return a.forEach(function(a) {
                            b = b && !!document.queryCommandSupported(a)
                        }),
                        b
                    }
                }],
                (f = [{
                    key: "resolveOptions",
                    value: function() {
                        var a = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {};
                        this.action = "function" == typeof a.action ? a.action : this.defaultAction,
                        this.target = "function" == typeof a.target ? a.target : this.defaultTarget,
                        this.text = "function" == typeof a.text ? a.text : this.defaultText,
                        this.container = "object" === c(a.container) ? a.container : document.body
                    }
                }, {
                    key: "listenClick",
                    value: function(a) {
                        var b = this;
                        this.listener = m()(a, "click", function(a) {
                            return b.onClick(a)
                        })
                    }
                }, {
                    key: "onClick",
                    value: function(a) {
                        a = a.delegateTarget || a.currentTarget,
                        this.clipboardAction && (this.clipboardAction = null),
                        this.clipboardAction = new i({
                            action: this.action(a),
                            target: this.target(a),
                            text: this.text(a),
                            container: this.container,
                            trigger: a,
                            emitter: this
                        })
                    }
                }, {
                    key: "defaultAction",
                    value: function(a) {
                        return e("action", a)
                    }
                }, {
                    key: "defaultTarget",
                    value: function(a) {
                        if (a = e("target", a),
                        a)
                            return document.querySelector(a)
                    }
                }, {
                    key: "defaultText",
                    value: function(a) {
                        return e("text", a)
                    }
                }, {
                    key: "destroy",
                    value: function() {
                        this.listener.destroy(),
                        this.clipboardAction && (this.clipboardAction.destroy(),
                        this.clipboardAction = null)
                    }
                }]) && k(b.prototype, f),
                d && k(b, d),
                a
            }()
        },
        828: function(b) {
            var a;
            "undefined" == typeof Element || Element.prototype.matches || ((a = Element.prototype).matches = a.matchesSelector || a.mozMatchesSelector || a.msMatchesSelector || a.oMatchesSelector || a.webkitMatchesSelector),
            b.exports = function(a, b) {
                for (; a && 9 !== a.nodeType; ) {
                    if ("function" == typeof a.matches && a.matches(b))
                        return a;
                    a = a.parentNode
                }
            }
        },
        438: function(b, e, c) {
            var d = c(828);
            function a(a, f, b, g, c) {
                var e = function(a, b, e, c) {
                    return function(e) {
                        e.delegateTarget = d(e.target, b),
                        e.delegateTarget && c.call(a, e)
                    }
                }
                .apply(this, arguments);
                return a.addEventListener(b, e, c),
                {
                    destroy: function() {
                        a.removeEventListener(b, e, c)
                    }
                }
            }
            b.exports = function(b, d, c, e, f) {
                return "function" == typeof b.addEventListener ? a.apply(null, arguments) : "function" == typeof c ? a.bind(null, document).apply(null, arguments) : ("string" == typeof b && (b = document.querySelectorAll(b)),
                Array.prototype.map.call(b, function(b) {
                    return a(b, d, c, e, f)
                }))
            }
        },
        879: function(b, a) {
            a.node = function(a) {
                return void 0 !== a && a instanceof HTMLElement && 1 === a.nodeType
            }
            ,
            a.nodeList = function(b) {
                var c = Object.prototype.toString.call(b);
                return void 0 !== b && ("[object NodeList]" === c || "[object HTMLCollection]" === c) && "length"in b && (0 === b.length || a.node(b[0]))
            }
            ,
            a.string = function(a) {
                return "string" == typeof a || a instanceof String
            }
            ,
            a.fn = function(a) {
                return "[object Function]" === Object.prototype.toString.call(a)
            }
        },
        370: function(c, e, b) {
            var a = b(879)
              , d = b(438);
            c.exports = function(b, c, e) {
                if (!b && !c && !e)
                    throw new Error("Missing required arguments");
                if (!a.string(c))
                    throw new TypeError("Second argument must be a String");
                if (!a.fn(e))
                    throw new TypeError("Third argument must be a Function");
                if (a.node(b))
                    return i = c,
                    j = e,
                    (k = b).addEventListener(i, j),
                    {
                        destroy: function() {
                            k.removeEventListener(i, j)
                        }
                    };
                if (a.nodeList(b))
                    return f = b,
                    g = c,
                    h = e,
                    Array.prototype.forEach.call(f, function(a) {
                        a.addEventListener(g, h)
                    }),
                    {
                        destroy: function() {
                            Array.prototype.forEach.call(f, function(a) {
                                a.removeEventListener(g, h)
                            })
                        }
                    };
                if (a.string(b))
                    return b = b,
                    c = c,
                    e = e,
                    d(document.body, b, c, e);
                throw new TypeError("First argument must be a String, HTMLElement, HTMLCollection, or NodeList");
                var f, g, h, k, i, j
            }
        },
        817: function(a) {
            a.exports = function(a) {
                var c, b = "SELECT" === a.nodeName ? (a.focus(),
                a.value) : "INPUT" === a.nodeName || "TEXTAREA" === a.nodeName ? ((c = a.hasAttribute("readonly")) || a.setAttribute("readonly", ""),
                a.select(),
                a.setSelectionRange(0, a.value.length),
                c || a.removeAttribute("readonly"),
                a.value) : (a.hasAttribute("contenteditable") && a.focus(),
                b = window.getSelection(),
                (c = document.createRange()).selectNodeContents(a),
                b.removeAllRanges(),
                b.addRange(c),
                b.toString());
                return b
            }
        },
        279: function(b) {
            function a() {}
            a.prototype = {
                on: function(a, c, d) {
                    var b = this.e || (this.e = {});
                    return (b[a] || (b[a] = [])).push({
                        fn: c,
                        ctx: d
                    }),
                    this
                },
                once: function(b, c, d) {
                    var e = this;
                    function a() {
                        e.off(b, a),
                        c.apply(d, arguments)
                    }
                    return a._ = c,
                    this.on(b, a, d)
                },
                emit: function(c) {
                    for (var d = [].slice.call(arguments, 1), b = ((this.e || (this.e = {}))[c] || []).slice(), a = 0, e = b.length; a < e; a++)
                        b[a].fn.apply(b[a].ctx, d);
                    return this
                },
                off: function(c, d) {
                    var e = this.e || (this.e = {}), a = e[c], f = [], b, g;
                    if (a && d)
                        for (b = 0,
                        g = a.length; b < g; b++)
                            a[b].fn !== d && a[b].fn._ !== d && f.push(a[b]);
                    return f.length ? e[c] = f : delete e[c],
                    this
                }
            },
            b.exports = a,
            b.exports.TinyEmitter = a
        }
    },
    b = {},
    a.n = function(b) {
        var c = b && b.__esModule ? function() {
            return b.default
        }
        : function() {
            return b
        }
        ;
        return a.d(c, {
            a: c
        }),
        c
    }
    ,
    a.d = function(d, c) {
        for (var b in c)
            a.o(c, b) && !a.o(d, b) && Object.defineProperty(d, b, {
                enumerable: !0,
                get: c[b]
            })
    }
    ,
    a.o = function(a, b) {
        return Object.prototype.hasOwnProperty.call(a, b)
    }
    ,
    a(134).default;
    function a(d) {
        if (b[d])
            return b[d].exports;
        var e = b[d] = {
            exports: {}
        };
        return c[d](e, e.exports, a),
        e.exports
    }
    var c, b
}),
function() {
    'use strict';
    var a, d, f, b, c, g, e;
    document.querySelectorAll('.tooltip-demo').forEach(function(a) {
        new bootstrap.Tooltip(a,{
            selector: '[data-bs-toggle="tooltip"]'
        })
    }),
    document.querySelectorAll('[data-bs-toggle="popover"]').forEach(function(a) {
        new bootstrap.Popover(a)
    }),
    a = document.getElementById('toastPlacement'),
    a && document.getElementById('selectToastPlacement').addEventListener('change', function() {
        a.dataset.originalClass || (a.dataset.originalClass = a.className),
        a.className = a.dataset.originalClass + ' ' + this.value
    }),
    document.querySelectorAll('.bd-example .toast').forEach(function(a) {
        var b = new bootstrap.Toast(a,{
            autohide: !1
        });
        b.show()
    }),
    d = document.getElementById('liveToastBtn'),
    f = document.getElementById('liveToast'),
    d && d.addEventListener('click', function() {
        var a = new bootstrap.Toast(f);
        a.show()
    }),
    document.querySelectorAll('.tooltip-test').forEach(function(a) {
        new bootstrap.Tooltip(a)
    }),
    document.querySelectorAll('.popover-test').forEach(function(a) {
        new bootstrap.Popover(a)
    }),
    document.querySelectorAll('.bd-example-indeterminate [type="checkbox"]').forEach(function(a) {
        a.indeterminate = !0
    }),
    document.querySelectorAll('.bd-content [href="#"]').forEach(function(a) {
        a.addEventListener('click', function(a) {
            a.preventDefault()
        })
    }),
    b = document.getElementById('exampleModal'),
    b && b.addEventListener('show.bs.modal', function(c) {
        var d = c.relatedTarget
          , a = d.getAttribute('data-bs-whatever')
          , e = b.querySelector('.modal-title')
          , f = b.querySelector('.modal-body input');
        e.textContent = 'New message to ' + a,
        f.value = a
    }),
    c = document.getElementById('btnToggleAnimatedProgress'),
    c && c.addEventListener('click', function() {
        c.parentNode.querySelector('.progress-bar-striped').classList.toggle('progress-bar-animated')
    }),
    g = '<div class="bd-clipboard"><button type="button" class="btn-clipboarda uk-button uk-button-default" title="Copy to clipboard" style="width: 3px;"><span uk-icon="icon: copy"></span></button></div>',
    document.querySelectorAll('div.highlight').forEach(function(a) {
        a.insertAdjacentHTML('beforebegin', g)
    }),
    document.querySelectorAll('.btn-clipboarda').forEach(function(a) {
        var b = new bootstrap.Tooltip(a);
        a.addEventListener('mouseleave', function() {
            b.hide()
        })
    }),
    e = new ClipboardJS('.btn-clipboarda',{
        target: function(a) {
            return a.parentNode.nextElementSibling
        }
    }),
    e.on('success', function(a) {
        var b = bootstrap.Tooltip.getInstance(a.trigger);
        a.trigger.setAttribute('data-bs-original-title', 'Copied!'),
        b.show(),
        a.trigger.setAttribute('data-bs-original-title', 'Copy to clipboard'),
        a.clearSelection()
    }),
    e.on('error', function(a) {
        var b = /mac/i.test(navigator.userAgent) ? '\u2318' : 'Ctrl-'
          , c = 'Press ' + b + 'C to copy'
          , d = bootstrap.Tooltip.getInstance(a.trigger);
        a.trigger.setAttribute('data-bs-original-title', c),
        d.show(),
        a.trigger.setAttribute('data-bs-original-title', 'Copy to clipboard')
    }),
    anchors.options = {
        icon: '#'
    },
    anchors.add('.bd-content > h2, .bd-content > h3, .bd-content > h4, .bd-content > h5')
}()

